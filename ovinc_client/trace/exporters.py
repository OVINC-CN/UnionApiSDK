import threading
from typing import Sequence

from opentelemetry.sdk.trace import ReadableSpan
from opentelemetry.sdk.trace.export import BatchSpanProcessor, SpanExporter, SpanExportResult


class LazyBatchSpanProcessor(BatchSpanProcessor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.done = True
        with self.condition:
            self.condition.notify_all()
        self.worker_thread.join()
        self.done = False
        self.worker_thread = None

    def on_end(self, span: ReadableSpan) -> None:
        if self.worker_thread is None:
            self.worker_thread = threading.Thread(name=self.__class__.__name__, target=self.worker, daemon=True)
            self.worker_thread.start()
        super().on_end(span)

    def shutdown(self) -> None:
        self.done = True
        with self.condition:
            self.condition.notify_all()
        if self.worker_thread:
            self.worker_thread.join()
        self.span_exporter.shutdown()


class NoOpSpanExporter(SpanExporter):
    """不执行任何操作的 Span Exporter，用于禁用数据上报时使用"""

    def export(self, spans: Sequence[ReadableSpan]) -> SpanExportResult:
        return SpanExportResult.SUCCESS

    def shutdown(self) -> None:
        pass
