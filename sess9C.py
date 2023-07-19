class Patient:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.next = None
        self.previous = None

    def show(self):
        print(f"Name:{self.name}, Age:{self.age}, Gender:{self.gender}")


class PatientQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, patient):
        self.size += 1

        if self.head is None:
            self.head = patient
            self.tail = patient
        else:
            self.tail.next = patient
            patient.previous = self.tail

            # Any new patient to the end of queue :)
            self.tail = patient
            # Delete the first object i.e. Patient

    def dequeue(self):

        if self.size != 0:
            self.size -= 1
            self.head = self.head.next
        else:
            print("Queue is empty :)")

    def iterate(self):
        if self.size > 0:
            temp = self.head
            while True:
                temp.show()
                temp = temp.next

                if temp is None:
                    break

        else:
            print("Queue is Empty. Cannot Iterate")


patient1 = Patient(name="John", age=20, gender="male")
patient2 = Patient(name="fionna", age=29, gender="female")

print("Patient1:")
print(patient1)

print("Patient2:")
print(patient2)
