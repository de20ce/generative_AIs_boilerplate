#!/bin/bash
# fails if any command in your code fails
set -o errexit
# exit if any of pipe command fails
set -o pipefail
# exit if any variable is not set
set -o nounset


celery --app=core worker --loglevel=info