from bears.scss.SCSSLintBear import SCSSLintBear
from tests.LocalBearTestHelper import verify_local_bear


good_file = """
.btn-primary {
  &:hover {
    background-color: darken($btn-primary-bg, 3%);
  }
}
"""

bad_file = """
.btn-primary {
  &:hover {
    background-color: darken($btn-primary-bg, 3%)
}
"""


SCSSLintBearTest = verify_local_bear(SCSSLintBear,
                                     valid_files=(good_file,),
                                     invalid_files=(bad_file,))
