from servidor import complete_task, get_task

RAM_MAXIMA_GB = 5


def executed_pipeline(homework_name):

    task_found = get_task(homework_name)

    if task_found is None:
        print("Error. The task does not exist in the system.")
        return False

    if task_found["requisito_ram_gb"] <= RAM_MAXIMA_GB:
        complete_task(homework_name)
        print(f"Succes! Task {homework_name} executed and state updated and completed.")
        return True
    else:
        print(
            f"Alert: There are not enough resources for {homework_name}. Require {task_found['requisito_ram_gb']}GB and the limit is {RAM_MAXIMA_GB}GB."
        )

        return False
