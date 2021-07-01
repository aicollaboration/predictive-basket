# Predictive basket service

## Pipelines

### Build

- docker login -u "$DOCKER_USER" -p "$DOCKER_PASSWORD" docker.io
- docker build --cache-from "5elementsofai/text-summarization:latest" --tag "5elementsofai/text-summarization:latest" --tag "5elementsofai/text-summarization:$CI_COMMIT_SHA" .
- docker push "5elementsofai/text-summarization:$CI_COMMIT_SHA"

### Deploy

- kubectl config set-cluster "$CLUSTER_NAME" --server="$URL" --insecure-skip-tls-verify=true
- kubectl config set-credentials "$USER" --token="$TOKEN"
- kubectl config set-context "$CONTEXT" --cluster="$CLUSTER_NAME" --user="$USER"
- kubectl config use-context "$CONTEXT"
- helm upgrade --install aiplatform-text-summarization charts -f charts/values.yaml --set tag=$CI_COMMIT_SHA
