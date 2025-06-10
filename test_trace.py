from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

exporter = OTLPSpanExporter(
    endpoint="https://otlp.kloudmate.com/v1/traces",
    headers={"Authorization": "sk_m99L18ibJKWZvJffRH5RD2LB"},
)

span_processor = BatchSpanProcessor(exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

with tracer.start_as_current_span("manual-span-kloudmate"):
    print("Span sent to KloudMate dashboard successfully")
