import hashlib
import json
from datetime import datetime


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps(
            {
                "index": self.index,
                "timestamp": self.timestamp,
                "data": self.data,
                "previous_hash": self.previous_hash,
            },
            sort_keys=True,
        )
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        data = {
            "Certificate ID": "0",
            "Student Name": "Genesis",
            "Degree": "None",
            "Year": "0000",
        }
        return Block(0, str(datetime.now()), data, "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_certificate(self, cert_id, name, degree, year):
        data = {
            "Certificate ID": cert_id,
            "Student Name": name,
            "Degree": degree,
            "Year": year,
        }
        new_block = Block(
            len(self.chain),
            str(datetime.now()),
            data,
            self.get_latest_block().hash,
        )
        self.chain.append(new_block)

    def display_blockchain(self):
        print("\n========== BLOCKCHAIN ==========")
        for block in self.chain:
            print("\nBlock:", block.index)
            print("Timestamp:", block.timestamp)
            print("Certificate Details:", block.data)
            print("Previous Hash:", block.previous_hash)
            print("Hash:", block.hash)

    def verify_blockchain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                print("\nBlockchain Compromised!")
                return False

            if current.previous_hash != previous.hash:
                print("\nBlockchain Compromised!")
                return False

        print("\nBlockchain is Secure.")
        return True

    def search_certificate(self, cert_id):
        for block in self.chain:
            if block.data["Certificate ID"] == cert_id:
                print("\nCertificate Found")
                print(block.data)
                return
        print("\nCertificate Not Found.")

    def tamper_block(self, index):
        if index < len(self.chain):
            self.chain[index].data["Student Name"] = "Hacker"


blockchain = Blockchain()

while True:
    print("\n====== Digital Certificate Verification System ======")
    print("1. Add Certificate")
    print("2. Display Blockchain")
    print("3. Verify Blockchain")
    print("4. Search Certificate")
    print("5. Tamper Block")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        cid = input("Certificate ID: ")
        name = input("Student Name: ")
        degree = input("Degree: ")
        year = input("Year: ")
        blockchain.add_certificate(cid, name, degree, year)
        print("Certificate Added Successfully.")

    elif choice == "2":
        blockchain.display_blockchain()

    elif choice == "3":
        blockchain.verify_blockchain()

    elif choice == "4":
        cid = input("Enter Certificate ID: ")
        blockchain.search_certificate(cid)

    elif choice == "5":
        index = int(input("Enter Block Number to Tamper: "))
        blockchain.tamper_block(index)
        print("Block Tampered.")

    elif choice == "6":
        print("Thank You.")
        break

    else:
        print("Invalid Choice.")
