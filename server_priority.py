import heapq
from datetime import datetime


class PriorityQueue:
    def __init__(self):
        self.priority_queue = []  
        self.statistics = []     
    
    # Add request first
    def add_request(self, priority, name):
        print("=" * 70)
        timestamp = datetime.now() 
        heapq.heappush(self.priority_queue, (priority, name))
        self.statistics.append({"name": name, "priority": priority, "time": timestamp})
        print(f"    ✅ Request added: Name={name}, Priority={priority}, Time={timestamp} ✅")
    
    # Then process it
    def process_request(self):
        print("=" * 70)
        print("\n🔄 Processing the next request...")
        if self.priority_queue:
            priority, name = heapq.heappop(self.priority_queue)
            print(f"    🔄Processing request: Name={name}, Priority={priority}🔄")
            return priority, name
        else:
            print("     ⚠️ There is nothing to process...")
    
    def show_statistics(self):
        print("=" * 70)
        print("\nRequest Statistics:")
        for stat in self.statistics:
            print(
                f"User: {stat['name']}, Priority: {stat['priority']}, Time: {stat['time']}"
            )
        print()
    
    def __str__(self):
        print("=" * 70)
        if not self.priority_queue:
            return "    ⚠️The request queue is empty...."
        
        result = ["Current Request Queue:"]
        for priority, task in sorted(self.priority_queue): 
            result.append(f"    👋 Task: {task}   |    Priority: {priority} 👋")
        
        return "\n".join(result)
    



Running = True
active_queue = PriorityQueue()
menu = """
Menu Options:
1. Add a request to the queue
2. Show the current queue
3. Process the next request
4. Show request history
5. Quit the program
"""

print("Starting program! \n")
while Running : 
    print(menu)
    choice = input("What do you want to do?: ")
    # Add request to the queue 
    if choice == "1":   
        name = input("Enter your nickname: ")
        try:
            priority = int(input("Enter your priority (lower numbers = higher priority): "))
            active_queue.add_request(priority, name)
        except ValueError:
            print("    ❌ Invalid priority! Please enter a number.")
    # Show current queue
    elif choice == "2": 
        print(active_queue)  
    # Process the queue
    elif choice == "3":  
        active_queue.process_request() 
    # Show history of queue
    elif choice == "4": 
        active_queue.show_statistics()  
    # Byebye
    elif choice == "5": 
        print("Exiting the program. Goodbye!")
        Running = False
    else: 
        print("    ❌ Invalid input! Please choose a valid option.")
    print("=" * 70)

    
