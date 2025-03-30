import random
from datetime import datetime, timedelta

# Expanded patient database with more demographic information
patients = [
    {"id": 1, "name": "Ravi Kumar", "age": 68, "language": "Tamil", "channel": "SMS", "tech_comfort": "LOW"},
    {"id": 2, "name": "Ananya Rao", "age": 35, "language": "Telugu", "channel": "WhatsApp", "tech_comfort": "HIGH"},
    {"id": 3, "name": "Joseph Mathew", "age": 72, "language": "Malayalam", "channel": "IVR", "tech_comfort": "LOW"},
    {"id": 4, "name": "Rahul Sharma", "age": 42, "language": "Hindi", "channel": "SMS", "tech_comfort": "MEDIUM"},
    {"id": 5, "name": "David Thomas", "age": 31, "language": "English", "channel": "WhatsApp", "tech_comfort": "HIGH"},
    {"id": 6, "name": "Lakshmi Venkatesh", "age": 70, "language": "Tamil", "channel": "IVR", "tech_comfort": "LOW"},
    {"id": 7, "name": "Priya Reddy", "age": 29, "language": "Telugu", "channel": "WhatsApp", "tech_comfort": "HIGH"},
    {"id": 8, "name": "Samir Khan", "age": 50, "language": "Hindi", "channel": "SMS", "tech_comfort": "MEDIUM"},
    {"id": 9, "name": "Arun Nair", "age": 45, "language": "Malayalam", "channel": "SMS", "tech_comfort": "MEDIUM"},
    {"id": 10, "name": "Jennifer Wilson", "age": 38, "language": "English", "channel": "WhatsApp", "tech_comfort": "HIGH"},
]

# Expanded message templates for different purposes
message_templates = {
    "appointment_reminder": {
        "Tamil": {
            "standard": "உங்கள் {doctor} டாக்டரிடம் {date} அன்று {time} மணிக்கு அப்பாய்ண்ட்மென்ட் உள்ளது. உறுதிப்படுத்த YES என பதிலளிக்கவும்.",
            "elderly": "நினைவூட்டல்: {date}, {time} மருத்துவர் {doctor} சந்திப்பு. உறுதிப்படுத்த YES என பதிலளிக்கவும்."
        },
        "Telugu": {
            "standard": "మీరు {date} న {time} కి {doctor} డాక్టర్‌తో అపాయింట్‌మెంట్ ఉంది. నిర్ధారించడానికి YES అని సమాధానం ఇవ్వండి.",
            "elderly": "రిమైండర్: {date}, {time} కి డాక్టర్ {doctor} తో అపాయింట్మెంట్. నిర్ధారించడానికి YES అని సమాధానం."
        },
        "Malayalam": {
            "standard": "നിങ്ങൾക്ക് {date} ന് {time} മണിക്ക് ഡോക്ടർ {doctor} മായി അപ്പോയിന്റ്മെന്റ് ഉണ്ട്. സ്ഥിരീകരിക്കാൻ YES എന്ന് മറുപടി നൽകുക.",
            "elderly": "ഓർമ്മപ്പെടുത്തൽ: {date}, {time} ന് ഡോക്ടർ {doctor} മായി അപ്പോയിന്റ്മെന്റ്. സ്ഥിരീകരിക്കാൻ YES എന്ന് മറുപടി നൽകുക."
        },
        "Hindi": {
            "standard": "आपका डॉक्टर {doctor} के साथ {date} को {time} बजे अपॉइंटमेंट है। पुष्टि के लिए YES जवाब दें।",
            "elderly": "अनुस्मारक: {date}, {time} पर डॉक्टर {doctor} के साथ अपॉइंटमेंट। पुष्टि के लिए YES जवाब दें।"
        },
        "English": {
            "standard": "You have an appointment with Dr. {doctor} on {date} at {time}. Reply YES to confirm.",
            "elderly": "REMINDER: Appointment with Dr. {doctor} on {date}, {time}. Reply YES to confirm."
        }
    },
    "wait_time": {
        "Tamil": "தற்போதைய காத்திருப்பு நேரம்: {wait_time} நிமிடங்கள். தயவுசெய்து அதற்கேற்ப திட்டமிடவும்.",
        "Telugu": "ప్రస్తుత వేచి ఉండే సమయం: {wait_time} నిమిషాలు. దయచేసి అందుకు తగినట్లుగా ప్లాన్ చేయండి.",
        "Malayalam": "നിലവിലെ കാത്തിരിപ്പ് സമയം: {wait_time} മിനിറ്റ്. ദയവായി അതനുസരിച്ച് പ്ലാൻ ചെയ്യുക.",
        "Hindi": "वर्तमान प्रतीक्षा समय: {wait_time} मिनट। कृपया तदनुसार योजना बनाएं।",
        "English": "Current wait time: {wait_time} minutes. Please plan accordingly."
    },
    "prescription_reminder": {
        "Tamil": "உங்கள் {medication} மருந்துகளை {frequency} எடுத்துக்கொள்ள நினைவூட்டல். மீண்டும் நிரப்ப வேண்டுமானால் REFILL என்று பதிலளிக்கவும்.",
        "Telugu": "మీ {medication} మందులను {frequency} తీసుకోవడానికి రిమైండర్. రీఫిల్ కావాలంటే REFILL అని సమాధానం ఇవ్వండి.",
        "Malayalam": "നിങ്ങളുടെ {medication} മരുന്ന് {frequency} കഴിക്കാൻ ഓർമ്മപ്പെടുത്തൽ. റീഫിൽ വേണമെങ്കിൽ REFILL എന്ന് മറുപടി നൽകുക.",
        "Hindi": "आपकी {medication} दवा {frequency} लेने के लिए रिमाइंडर। रिफिल चाहिए तो REFILL जवाब दें।",
        "English": "Reminder to take your {medication} {frequency}. Reply REFILL if you need a refill."
    }
}

# Channel-specific sending functions
def send_sms(patient, message):
    print(f"📱 SMS to {patient['name']}: {message}")
    return True

def send_whatsapp(patient, message):
    print(f"💬 WhatsApp to {patient['name']}: {message}")
    return True

def send_ivr(patient, message):
    print(f"☎️ Voice Call to {patient['name']}: \"{message}\"")
    return True

# Smart channel selection based on patient demographics and preferences
def determine_best_channel(patient):
    # Use existing channel preference if available
    if "channel" in patient:
        return patient["channel"]
    
    # Otherwise, make a recommendation based on demographics
    if patient["age"] > 65 and patient["tech_comfort"] == "LOW":
        return "IVR"
    elif patient["tech_comfort"] == "HIGH":
        return "WhatsApp"
    else:
        return "SMS"

# Message template selection based on patient demographics
def select_message_template(patient, message_type, data):
    language = patient["language"]
    
    # Default to English if language not available
    if language not in message_templates[message_type]:
        language = "English"
    
    # Use elderly-friendly templates for seniors
    if message_type == "appointment_reminder" and patient["age"] > 65:
        template = message_templates[message_type][language]["elderly"]
    elif message_type == "appointment_reminder":
        template = message_templates[message_type][language]["standard"]
    else:
        template = message_templates[message_type][language]
    
    # Fill in the template with the provided data
    for key, value in data.items():
        template = template.replace("{" + key + "}", str(value))
    
    return template

# Unified function to send a message through the appropriate channel
def send_message(patient, message_type, data):
    # Select the appropriate template and fill in the data
    message = select_message_template(patient, message_type, data)
    
    # Determine the best channel for this patient
    channel = determine_best_channel(patient)
    
    # Send through the appropriate channel
    if channel == "SMS":
        return send_sms(patient, message)
    elif channel == "WhatsApp":
        return send_whatsapp(patient, message)
    elif channel == "IVR":
        return send_ivr(patient, message)
    else:
        return send_sms(patient, message)  # Default to SMS

# Effectiveness measurement with A/B testing capability
def measure_effectiveness(patients, test_group=None, control_group=None):
    """
    Measure the effectiveness of the messaging system, with optional A/B testing
    
    Args:
        patients (list): List of all patients
        test_group (list, optional): Test group patient IDs
        control_group (list, optional): Control group patient IDs
    """
    if test_group and control_group:
        # A/B testing mode
        test_confirmed = sum(1 for p_id in test_group if random.random() < 0.75)  # 75% confirmation for test group
        control_confirmed = sum(1 for p_id in control_group if random.random() < 0.35)  # 35% confirmation for control
        
        test_rate = (test_confirmed / len(test_group)) * 100
        control_rate = (control_confirmed / len(control_group)) * 100
        
        print(f"\n📊 A/B Testing Results:")
        print(f"Test Group Confirmation Rate: {test_rate:.2f}%")
        print(f"Control Group Confirmation Rate: {control_rate:.2f}%")
        print(f"Improvement: {test_rate - control_rate:.2f}%")
        
        if test_rate > control_rate:
            print(f"✓ The new system shows a positive impact on confirmation rates.")
        else:
            print(f"✗ The new system does not show improvement over the control.")
    else:
        # Standard measurement
        confirmed = sum(1 for _ in patients if random.random() < 0.65)  # Assuming 65% confirmation with new system
        confirmation_rate = (confirmed / len(patients)) * 100
        print(f"\n✅ Overall Confirmation Rate: {confirmation_rate:.2f}%")

# Generate some sample appointments for testing
def generate_sample_appointments(patients, num_days=7):
    doctors = ["Rajan", "Priya", "Ahmed", "Suresh", "Meera"]
    appointments = []
    
    for i in range(num_days):
        appointment_date = (datetime.now() + timedelta(days=i+1)).strftime("%d-%b-%Y")
        
        # Generate 3-5 appointments per day
        for _ in range(random.randint(3, 5)):
            patient = random.choice(patients)
            doctor = random.choice(doctors)
            hour = random.randint(9, 16)
            minute = random.choice([0, 15, 30, 45])
            appointment_time = f"{hour}:{minute:02d} {'AM' if hour < 12 else 'PM'}"
            
            appointments.append({
                "patient_id": patient["id"],
                "patient": patient,
                "doctor": doctor,
                "date": appointment_date,
                "time": appointment_time,
                "wait_time": random.randint(5, 45)  # Random wait time 5-45 minutes
            })
    
    return appointments

# Simulate running the system
def run_simulation():
    print("🏥 Apollo Clinic Multi-Language Communication System Simulation")
    print("=" * 70)
    
    # Generate sample appointments
    appointments = generate_sample_appointments(patients)
    
    print(f"\n📅 Sending Appointment Reminders for {len(appointments)} upcoming appointments:")
    for appointment in appointments:
        patient = appointment["patient"]
        send_message(
            patient,
            "appointment_reminder", 
            {
                "doctor": appointment["doctor"],
                "date": appointment["date"],
                "time": appointment["time"]
            }
        )
    
    print("\n⏱️ Sending Wait Time Updates:")
    # Send wait time updates to a subset of patients with appointments today
    today_appointments = [a for a in appointments if "tomorrow" in a["date"].lower()]
    if not today_appointments:
        today_appointments = appointments[:3]  # Use first 3 if none for "tomorrow"
    
    for appointment in today_appointments:
        patient = appointment["patient"]
        send_message(
            patient,
            "wait_time",
            {"wait_time": appointment["wait_time"]}
        )
    
    print("\n💊 Sending Prescription Reminders:")
    # Send prescription reminders to a subset of patients
    medications = ["Metformin", "Atorvastatin", "Amlodipine", "Levothyroxine"]
    frequencies = ["daily", "twice daily", "with meals", "before bedtime"]
    
    for i in range(3):  # Send to 3 random patients
        patient = random.choice(patients)
        send_message(
            patient,
            "prescription_reminder",
            {
                "medication": random.choice(medications),
                "frequency": random.choice(frequencies)
            }
        )
    
    # Set up and run A/B testing
    # Divide patients into test and control groups
    all_patient_ids = [p["id"] for p in patients]
    random.shuffle(all_patient_ids)
    mid_point = len(all_patient_ids) // 2
    
    test_group = all_patient_ids[:mid_point]
    control_group = all_patient_ids[mid_point:]
    
    measure_effectiveness(patients, test_group, control_group)

# Run the simulation
if __name__ == "__main__":
    run_simulation()
