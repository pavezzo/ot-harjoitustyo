```mermaid
    sequenceDiagram
        Main ->> Machine: Machine()
        Machine ->> FuelTank: FuelTank()
        Machine ->> FuelTank: fill(40)
        Machine ->> Engine: Engine(tank)
        Machine -->> Main: 

        Main ->> Machine: drive()
        Machine ->> Engine: start()
        Engine ->> FuelTank: consume(5)
        Machine ->> Engine: is_running()
        Engine -->> Machine: True
        Machine ->> Engine: use_energy()
        Engine ->> FuelTank: consume(10)
        Machine -->> Main: 
```