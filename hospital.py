def input_valid_int(msg, start=0, end=None):
    while True:
        inp = input(msg)
        if not inp.isdecimal():
            print('Invalid input. Try again.')
        elif start is not None and end is not None:
            if not (start <= int(inp) <= end):
                print('Invalid input. Try again.')
            else: return int(inp)
        else: return int(inp)

class Patient:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __str__(self):
        return f'{self.name} is {self.status}'

    def __repr__(self):
        return f'{self.name} is {self.status}'

    def __lt__(self, other):
        return self.status < other.status

class HospitalManager:
    def __init__(self, specializations_cnt):
        self.specializations = [[] for i in range(specializations_cnt)]
        self.MAX_QUEUE = 10
        self.NORMAL = 0
        self.URGENT = 1
        self.SUPERURGENT = 2

    def can_add_more_patients(self , specialization):
        return len(self.specializations[specialization]) < self.MAX_QUEUE

    def add_patient_smart(self, specialization, name, status):
        spec = self.specializations[specialization]
        spec.append(Patient(name, status))
        spec.sort()

    def add_patient(self, specialization, name, status):
        spec = self.specializations[specialization]
        pat = Patient(name, status)
        if status == 0 or len(spec) == 0:
            spec.append(pat)
        elif status == 1:
            if spec[-1].status != self.NORMAL:
                spec.append(pat)
            else: #find the first normal and add before it
                for idx, patient in enumerate(spec):
                    if self.NORMAL == patient.status:
                        spec.insert(idx, pat)
                        break
        else:
            if spec[-1].status == self.SUPERURGENT:
                spec.append(pat)
            else:
                for idx, patient in enumerate(spec):
                    if patient.status == self.NORMAL or patient.status == self.URGENT:
                        spec.insert(idx, pat)
                        break

    def get_printable_patients_info(self):
        printable_patients_info = []
        for idx , specialization in enumerate(self.specializations):
            if not specialization:
                continue
            curr_patients_info = []
            for patient in specialization:
                curr_patients_info.append(str(patient))
            printable_patients_info.append((idx, curr_patients_info))
        return printable_patients_info


    def get_next_patients(self, specialization):
        if len(self.specializations[specialization]) == 0:
            return None
        return self.specializations[specialization].pop(0)

    def remove_patient(self, specialization, name):
        spec = self.specializations[specialization]
        for idx, patient in enumerate(spec):
            if patient.name == name:
                del spec[idx]
                return True
        return False

class FrontendManager:
    def __init__(self, specializations_cnt = 20):
        self.specializations_cnt = specializations_cnt
        self.hospital_manager = HospitalManager(self.specializations_cnt)
        self.add_dummy_data()

    def print_menu(self):
        print("\nProgram options:")
        messages = [
            'Add new patient',
            'Print all patients',
            'Get Next Patient',
            'Remove a leaving patient',
            'End the program'
        ]
        messages = [ f'{idx+1} {msg}' for idx, msg in enumerate(messages) ]
        print('\n'.join(messages))
        msg = f'Enter your choice (from 1 to {len(messages)}): '
        return input_valid_int(msg, 1 , len(messages))

    def add_dummy_data(self):
        for i in range(10):
            self.hospital_manager.add_patient(2, 'Dummy', i % 3)
        for i in range(4):
            self.hospital_manager.add_patient(5, 'AnotherDummy' + str(i), 0)
        for i in range(5):
            self.hospital_manager.add_patient(8, 'ThirdDummy' + str(i), 1)
        for i in range(3):
            self.hospital_manager.add_patient(12, 'ForthDummy' + str(i), 2)
        for i in range(3):
            self.hospital_manager.add_patient(13, 'FifthDummy' + str(i), 1)
            self.hospital_manager.add_patient(13, 'FifthDummy' + str(i + 5), 2)

    def run(self):
        while True:
            choice = self.print_menu()
            if choice == 1:
                specialization = input_valid_int('Enter specialization: ', 1, self.specializations_cnt )-1
                if self.hospital_manager.can_add_more_patients(specialization):
                    name = input('Enter patient name: ')
                    status = input_valid_int('Enter patient status (0 normal / 1 urgent / 2 super urgent: ', 0, 2)
                    self.hospital_manager.add_patient(specialization, name, status)
                else:
                   print('sorry we can not add patient, the specialization is full')
            elif choice == 2:
                results = self.hospital_manager.get_printable_patients_info()
                if not results:
                    print('No patients at the moment')
                else:
                    for idx, patient in results:
                        print(f'specialization {idx+1}: there are {len(patient)} patients')
                        print("\n".join(patient)+ '\n')
            elif choice == 3:
                specialization = input_valid_int('Enter specialization: ', 1, self.specializations_cnt )-1
                patient = self.hospital_manager.get_next_patients(specialization)
                if patient is None:
                   print('No patients at the moment')
                else:
                    print(f'{patient.name}, please go to the Dr')
            elif choice == 4:
                specialization = input_valid_int('Enter specialization: ', 1, self.specializations_cnt )-1
                name = input("Enter patient name: ")
                if not self.hospital_manager.remove_patient(specialization, name):
                    print('No patient with this name in this specialization')
            else:
                break

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = FrontendManager()
    app.add_dummy_data()
    app.run()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
