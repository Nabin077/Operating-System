#deadlock
class DeadlockAvoidance:
    def __init__(self, available_resources):
        self.available_resources = available_resources
        self.max_demand = {}
        self.allocation = {}
        self.need = {}

    def add_process(self, process_id, max_demand):
        self.max_demand[process_id] = max_demand
        self.allocation[process_id] = 0
        self.need[process_id] = max_demand

    def request_resources(self, process_id, request):
        if request > self.need[process_id]:
            print(f"Error: Process {process_id} has exceeded its maximum claim.")
            return False

        if request > self.available_resources:
            print(f"Process {process_id} must wait, resources not available.")
            return False

        # Pretend to allocate requested resources
        self.available_resources -= request
        self.allocation[process_id] += request
        self.need[process_id] -= request

        # Check system's state after allocation
        if self.check_safety():
            print(f"Resources allocated to Process {process_id}.")
            return True
        else:
            # Rollback
            self.available_resources += request
            self.allocation[process_id] -= request
            self.need[process_id] += request
            print(f"Process {process_id} must wait, state would be unsafe.")
            return False

    def check_safety(self):
        work = self.available_resources
        finish = {p: False for p in self.max_demand}

        while True:
            found = False
            for process_id, need in self.need.items():
                if not finish[process_id] and need <= work:
                    work += self.allocation[process_id]
                    finish[process_id] = True
                    found = True

            if not found:
                break

        return all(finish.values())

# Example usage
if __name__ == "__main__":
    # Initialize system with 10 available resources
    system = DeadlockAvoidance(available_resources=10)

    # Add processes with their maximum demands
    system.add_process("P1", 7)
    system.add_process("P2", 5)
    system.add_process("P3", 3)

    # Processes requesting resources
    system.request_resources("P1", 5)  # Should allocate resources
    system.request_resources("P2", 3)  # Should allocate resources
    system.request_resources("P3", 2)  # Should allocate resources
    system.request_resources("P1", 2)  # Should wait (if unsafe)
    system.request_resources("P3", 1)  # Should allocate resources
