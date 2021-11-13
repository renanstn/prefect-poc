# prefect-poc

## Setup do Server

Alterar o backend default para o server
```
prefect backend server
```

Iniciar o server
```
prefect server start
```

Pela UI, criar um project

Registrar seu flow com o comando:
```
flow.register(project_name="<nome do project criado via UI>")
```

Caos queira usar o scheduler, é necessário iniciar um Agent local também
```
prefect agent local start
```
