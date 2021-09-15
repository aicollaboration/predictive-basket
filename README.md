# Predictive basket service

## Pipelines

### Build

- docker login -u "$DOCKER_USER" -p "$DOCKER_PASSWORD" docker.io
- docker build --cache-from "aicollaboration/predictive-basket:latest" --tag "aicollaboration/predictive-basket:latest" --tag "aicollaboration/predictive-basket:add68f48eb6e990752b007b4abc272428376b669" .
- docker push "aicollaboration/predictive-basket:add68f48eb6e990752b007b4abc272428376b669"

### Deploy

- kubectl config set-cluster "$CLUSTER_NAME" --server="$URL" --insecure-skip-tls-verify=true
- kubectl config set-credentials "$USER" --token="$TOKEN"
- kubectl config set-context "$CONTEXT" --cluster="$CLUSTER_NAME" --user="$USER"
- kubectl config use-context "$CONTEXT"
- helm upgrade --install aicollaboration-service-predictive-basket charts -f charts/values.yaml --set tag=$CI_COMMIT_SHA
