from lean_dojo import *

repo = LeanGitRepo("https://github.com/Mohammad-Amjed/lean-question", "5a0360e49946815cb53132638ccdd46fb1859e2a")
theorem = Theorem(repo, "src/example.lean", "hello_world")

with Dojo(theorem) as (dojo, init_state):
  print(init_state)
  result = dojo.run_tac(init_state, "exact h")
  assert isinstance(result, ProofFinished)
  print(result)