import pathlib
import wfcommons
from wfcommons import BlastRecipe
from wfcommons.wfbench import WorkflowBenchmark

# create a synthetic workflow instance with 500 tasks or use one that you already have
workflow = BlastRecipe.from_num_tasks(500).build_workflow()
# create a workflow benchmark object to generate specifications based on a recipe
benchmark = WorkflowBenchmark(recipe=BlastRecipe, num_tasks=500)
# generate a specification based on performance characteristics and the structure of the synthetic workflow instance
path = benchmark.create_benchmark_from_synthetic_workflow(pathlib.Path("/tmp/"), workflow, cpu_work=100, percent_cpu=0.6)
