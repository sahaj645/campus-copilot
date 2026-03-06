VIT AI Copilot
A Unified AI Assistant for Everything on Campus

VIT AI Copilot is an intelligent assistant designed to simplify how students interact with campus services at the Vellore Institute of Technology.

University campuses involve hundreds of daily interactions — finding classrooms, reporting infrastructure issues, discovering events, booking facilities, understanding academic processes, and navigating campus resources.

Today, these tasks are spread across multiple platforms such as:

VTOP

Emails

WhatsApp groups

Notice boards

Department portals

Manual complaint systems

VIT AI Copilot introduces a single conversational interface that allows students to interact with campus services naturally.

Instead of searching through multiple platforms, students can simply describe what they need, and the system determines the best way to help.

The Idea

Campus interactions are intent-driven, not platform-driven.

Students rarely think in terms of which system to open.
They think in terms of problems they want to solve.

Examples of real situations:

A student cannot find their classroom

A projector stops working during a lecture

Someone wants to attend an event but doesn’t know where it is

A hostel resident needs to report a maintenance issue

A student wants to book a sports facility

Someone wants to know what is happening on campus today

VIT AI Copilot focuses on understanding the intent behind these situations and connecting students to the right service automatically.

What the Copilot Does

The AI assistant acts as a central coordination layer for campus services.

When a student makes a request, the system:

Understands the request using natural language processing

Identifies the type of problem or intent

Determines the appropriate campus service

Executes the action or retrieves the relevant information

Responds with actionable guidance

The goal is to make campus services accessible through conversation rather than navigation.

Example Real-World Scenarios
Getting Help on Campus

A student may ask how to reach a specific classroom, building, or facility.

The system can provide guidance by using campus location data, walking paths, and building information to help students reach their destination.

Instead of only returning the building name, the assistant can provide:

directions

estimated walking time

floor and room location details

nearby landmarks

Reporting Infrastructure Issues

When infrastructure problems occur during classes or in hostels, students usually rely on informal communication or manual complaint processes.

The Copilot allows students to report issues directly.

Examples of problems that can be reported:

Classroom equipment malfunction

WiFi connectivity issues

Water or electricity problems in hostels

Broken infrastructure in campus buildings

The system can automatically generate a complaint ticket and route it to the appropriate department.

Discovering Campus Events

Many students miss events because information is scattered across different groups and announcements.

The Copilot helps students discover:

workshops

technical events

club activities

hackathons

campus gatherings

Students can ask about events happening today, this week, or within specific categories.

Academic Assistance

Students often have questions related to academic processes.

Examples include:

course registration timelines

timetable information

leave application procedures

academic deadlines

The assistant can provide guidance and help students navigate academic workflows.

Facility Access and Booking

Students frequently use campus facilities such as sports complexes, study rooms, or event halls.

The Copilot can help students:

check facility availability

reserve time slots

locate the facility

receive booking confirmation

General Campus Information

The assistant can also help with everyday questions related to campus life.

Examples include:

mess timings

campus service hours

library schedules

hostel policies

transportation within campus

System Architecture

The system is designed as a modular architecture where the AI assistant connects multiple campus services.

User Query
↓
React Chat Interface
↓
FastAPI Backend
↓
AI Intent Classification Layer
↓
Service Router
↓
Campus Service Modules

Service Modules include:

Navigation and Campus Information Service

Complaint Management Service

Event Discovery Service

Facility Booking Service

Academic Assistance Service

These services interact with a Campus Knowledge Base that stores structured campus information such as buildings, facilities, schedules, and services.

Technology Stack

Frontend

React
TailwindCSS

Backend

Python
FastAPI

AI Layer

Large Language Models for intent understanding and query processing

Database

MongoDB / Firebase

Project Structure

vit-ai-copilot

backend
├ api.py
├ ai_router.py
├ services
│ ├ complaint_service.py
│ ├ event_service.py
│ ├ booking_service.py
│ ├ navigation_service.py
│
└ requirements.txt

frontend
├ src
│ ├ App.js
│ ├ Chat.js
│ └ api.js

Installation

Clone the repository

git clone https://github.com/your-repository/vit-ai-copilot.git

cd vit-ai-copilot

Backend Setup

cd backend

pip install -r requirements.txt

uvicorn api:app --reload

Backend runs on

http://localhost:8000

Frontend Setup

cd frontend

npm install

npm start

Frontend runs on

http://localhost:3000

Impact

VIT AI Copilot simplifies how students interact with campus infrastructure and services.

Key benefits include:

faster access to campus information

simplified issue reporting

improved event discoverability

easier campus navigation

reduced administrative overhead

The system is designed to scale and support thousands of student interactions daily.

Future Improvements

Potential future enhancements include:

integration with official VTOP APIs

authentication through student IDs

voice-based campus assistant

mobile application version

real-time campus map integration

analytics dashboard for campus administration

Vision

The long-term vision is to create a unified AI layer for university campuses.

Instead of navigating multiple systems, students interact with their campus through a single intelligent interface.

This approach can extend beyond VIT and be adapted to universities worldwide.

Contributors

Sahaj Gaur

Yogdeep Benchimath