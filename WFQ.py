import time

priority = []
standard = []
economy = []


def get_file(path):
    with open(path) as data_file:
        return data_file.read()

def clean_string(stream):
    """
    Clean up the input stream by removing newline characters and splitting each line into a list of elements.
    
    Params:
    stream (str): The input stream of data.
    
    Returns:
    list: A list of cleaned-up elements.
    """
    washed_stream = []
    stream = stream.splitlines(True)
    for element in stream:
        if "\n" in element:
            washed_stream.append(element.replace("\n", "").split(" "))
        else:
            washed_stream.append(element)
    return washed_stream


def print_queues():
    """
    Print the contents of each queue: Priority, Standard, and Economy.
    """
    print("\nPriority")
    for item in priority:
        print(item)
    
    print("\nStandard")
    for item in standard:
        print(item)
    
    print("\nEconomy")
    for item in economy:
        print(item)


def set_queues(data):
    """
    Populate the queues (Priority, Standard, and Economy) based on the input data.
    
    Params:
    data (list): The cleaned-up input data containing information about name and their priority.
    """
    for item in data:
        name = item[1]
        match item[0].lower():
            case "p":
                priority.append(name)
            case "s":
                standard.append(name)
            case "e":
                economy.append(name)


def process_queues():
    """
    Process data in each queue according to their priority type.
    """
    while get_biggest() != 0:
        time.sleep(1)
        print("\n###### Processing ######")
        print("\nPriority")
        for _ in range(3):
            if len(priority) > 0:
                print(priority.pop(0))
            else:
                print("Empty")
        print("\nStandard")
        for _ in range(2):
            if len(standard) > 0:
                print(standard.pop(0))
            else:
                print("Empty")                
        print("\nEconomy")
        if len(economy) > 0:
            len(economy.pop(0))
            print(economy.pop(0)) 
        else:
            print("Empty")               


def get_biggest():
    """
    Determine the size of the largest queue.
    
    Returns:
    int: The size of the largest queue.
    """
    return max([len(priority), len(standard), len(economy)])


def main():
    """
    Main function to execute the program.
    """
    # The name of the data file may need to be changed. I set it as data.txt because it was easier
    data = get_file("data.txt")
    washed_stream = clean_string(data)
    set_queues(washed_stream)
    print_queues()
    process_queues()


if __name__ == "__main__":
    main()
