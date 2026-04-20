import importlib

def run_script(script_name):
    print(f"Executando {script_name}...")
    module = importlib.import_module(script_name)

    if hasattr(module, 'main'):
        module.main()
    
    else:
        raise Exception(f"{script_name} não possui função main()")

def main():
    run_script("Scripts.01_read")
    run_script("Scripts.01_create_tables")
    run_script("Scripts.02_load_data")  

if __name__ == "__main__":
    main()