# End_to_End_ML_project_with_MLFlow_AWS

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py

## Dagshub
MLFLOW_TRACKING_URI=https://dagshub.com/Kamalesh9483/End_to_End_ML_project_with_MLFlow_AWS.mlflow \
MLFLOW_TRACKING_USERNAME=Kamalesh9483 \
MLFLOW_TRACKING_PASSWORD=899e45d06f2885b1c0b6be61e4b2658207d1bbb7 \
python script.py


1. EC2 access : It is virtual machine
2. ECR: Elastic Container registry to save  docker image in aws

#Description: About the deployment
1. Build docker image of the source code
2. Push your docker image to ECR
3. Launch Your EC2 
4. Pull Your image from ECR in EC2
5. Lauch your docker image in EC2
