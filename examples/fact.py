"""

Example
Animal Fact

"""

import sra_py

# -----------------------------------------------------------------------------
# lets get a random cat fact
# https://github.com/Atidipt123/sra_py/blob/main/docs/endpoints.md#animal-facts
# -----------------------------------------------------------------------------

cat_fact = sra_py.fact("cat")

print(cat_fact)
