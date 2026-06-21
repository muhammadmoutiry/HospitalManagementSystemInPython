# Hospital Management System

A Python-based Hospital Management System that simulates patient queue management across multiple medical specializations.

## Features

* Manage 20 medical specializations.
* Each specialization supports up to 10 patients.
* Priority-based patient handling:

  * **Super Urgent** (Highest Priority)
  * **Urgent**
  * **Regular**
* Add new patients to a specialization.
* Retrieve the next patient for a doctor.
* Remove patients who decide to leave before consultation.
* Display all specialization queues.
* Dummy data generation for testing.
* Menu-driven console interface.

---

## Project Requirements

The system maintains:

* 20 medical specializations.
* Maximum of 10 patients per specialization.
* Priority queues based on patient status.

### Patient Priorities

| Status       | Priority |
| ------------ | -------- |
| Super Urgent | Highest  |
| Urgent       | Medium   |
| Regular      | Lowest   |

Patients are inserted into the queue according to their priority while preserving arrival order within the same priority level.

---

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* Lists and Queue Management
* Console-Based User Interface

---

## System Menu

```text
1) Add New Patient
2) Print All Patients
3) Get Next Patient
4) Remove Leaving Patient
5) Load Dummy Data
6) Exit
```

---

## Example

### Add Patient

```text
Enter Specialization: 3
Enter Name: Ahmed
Enter Status:
0 = Regular
1 = Urgent
2 = Super Urgent
```

### Get Next Patient

```text
Doctor of specialization 3:
Please see patient Ahmed
```

---

## Project Structure

```text
hospital-system/
│
├── hospital.py
├── README.md
```


---

## Running the Project

Clone the repository:


Run:

```bash
python3 main.py
```

---

## Learning Objectives

This project demonstrates:

* Object-Oriented Design
* Queue Management
* Priority Handling Algorithms
* Data Validation
* Software Testing with Dummy Data
* Clean Code Practices

---

## Future Improvements

* Save data to files or databases.
* Graphical User Interface (GUI).
* Appointment scheduling.
* Doctor management.
* Patient medical records.
* Web-based version using Flask or Django.

---

## Author

Muhammad

Senior Embedded Software Engineer

Skills:

* Python
* C/C++
* Embedded Systems
* Linux
* AUTOSAR
* Firmware Development

---

## License

This project is for educational and learning purposes.

