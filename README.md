Pacotes necessarios
criar uma venv
python -m venv nome_da_venv 
pip install boto3
pip install awscli 


1 - criar um usuario no IAM
2 - dar um nome ao usuario e clicar next
3 - selecionar "attach polices directly
4 - Create policies - JSON:
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::nome-do-seu-bucket/*"
    }
  ]
}

5 - Dar um nome para a a politica - Create
6 - Procurar a nova politica na busca pelo nome dado e dar ok
7 - Clicar no nome do usuario e depois em "Access Key 1" - "Create access key"
Selecionar "Local code" - Next - Copiar as informação da chave access key e secret access key
Essas informações deverão ser usadas no codigo

Para rodar o codigo:
python .\cred_aws.py
