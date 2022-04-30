from ctypes import sizeof


def main():
    path = "/home/fvm/info/tracefile/IBMObjectStoreTrace026Part0"
    with open(path) as myfile:
        head = [next(myfile) for x in range(100)]
        size = 10
        for i in range(0, len(head), size):
            lists = head[i:i+size]



        # for item in head:
        #     request_type = item.split(" ")[1].split(".")[1]
        #     if(request_type == "GET"):
        #         print("")
        #     object_id = item.split(" ")[2]
        #     if request_type !="DELETE":
        #         size = int(item.split(" ")[3])

def data_slice():
    path = "/home/fvm/info/tracefile/IBMObjectStoreTrace026Part0"
    with open(path) as myfile:
        head = [next(myfile) for x in range(100)]
        size = 10
        for i in range(0, len(head), size):
            lists = head[i:i+size]

if __name__ == "__main__":
    main()