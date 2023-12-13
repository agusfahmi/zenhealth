import google.generativeai as palm
import streamlit as st

def is_health_related(prompt):
    health_keywords = [
    "health", "disease", "sick", "doctor", "hospital", "medicine", "nutrition", "exercise", "healthy food",
    "diet pattern", "urination", "pee", "exercise", "immunization", "vaccination", "vaccine", "immune", "stress", "diet", "nutrition",
    "prevent urination", "prevent diabetes", "diabetes", "cholesterol", "blood", "blood pressure", "examination", "checked",
    "reproduction", "clean water", "urine", "cleanliness", "clean", "treatment", "therapy", "physical", "sleep", "recovery",
    "nutrition", "urine", "leukocytes", "nitrite", "urobilinogen", "protein", "ph", "blood", "ketones", "bilirubin", "glucose",
    "body", "dipstick", "healthy", "stress", "cause", "body weight", "weight", "body", "diabetes", "symptoms", "immune",
    "immunity", "asthma", "pressure", "keto", "hiccups", "flu", "kidney", "cholesterol", "eat", "drink", "beverage", "calories", "syndrome", "transplantation",
    "smell", "smelly", "hematuria", "bowl", "poop", "urinate", "throw", "water", "medical", "assistance", "infection", "tract", "urine", "inflammation",
    "cystitis", "bladder", "polycystic", "cancer", "prostate", "prostatitis", "cyst", "nephrotic", "hypertension", "hypotension", "impotence", "dysfunction",
    "erection", "urethra", "incontinence", "retention", "nephritis", "disorder", "endometriosis", "rvu", "reflux", "vesicoureteral", "urethritis",
    "pyelonephritis", "chronic", "vesicle", "rectum", "papillon", "lefevre", "alport", "medication", "foot pain",
    "mental health", "wellness", "lifestyle", "holistic health", "physical activity", "healthcare", "medical care",
    "stress management", "sleep hygiene", "mindfulness", "self-care", "cardiovascular", "respiratory", "digestive system",
    "musculoskeletal", "immune system", "neurological", "reproductive health", "childhood immunization", "maternal health",
    "elderly health", "health screening", "preventive care", "health education", "health promotion", "virus", "bacteria",
    "hygiene practices", "sanitation", "public health", "health policy", "health insurance", "genetic factors", "hereditary",
    "holistic medicine", "alternative medicine", "complementary medicine", "chronic conditions", "acute conditions", "mental illness",
    "cognitive health", "social health", "environmental health", "occupational health", "addiction", "substance abuse", "rehabilitation",
    "physical therapy", "occupational therapy", "health research", "clinical trials", "pharmaceuticals", "drug interactions",
    "medication side effects", "health technology", "telemedicine", "digital health", "medical breakthrough", "medical innovation",
    "health disparities", "health equity", "community health", "global health", "nutrition counseling", "physical fitness",
    "health monitoring", "health assessment", "vital signs", "heart rate", "BMI", "health screenings", "health diagnosis",
    "healthcare providers", "primary care", "specialist", "medical emergency", "emergency care", "first aid", "trauma care",
    "medical imaging", "diagnostic tests", "radiology", "laboratory tests", "blood tests", "urinalysis", "medical conditions",
    "infectious diseases", "chronic diseases", "autoimmune diseases", "genetic disorders", "mental health disorders", "cardiovascular diseases",
    "respiratory diseases", "diagnostic procedures", "treatment options", "medication management", "surgery", "rehabilitation services",
    "palliative care", "end-of-life care", "patient care", "patient advocacy", "health communication", "health literacy", "patient rights",
    "medical ethics", "healthcare system", "healthcare costs", "healthcare quality", "healthcare access", "healthcare reform",
    "alternative therapies", "mind-body connection", "holistic healing", "preventive medicine", "health tracking", "wearable technology",
    "health coaching", "medical advice", "online health resources", "nutrition labels", "dietary supplements", "herbal remedies",
    "fitness programs", "workplace health", "ergonomics", "occupational safety", "recreational activities", "fitness trends",
    "sports medicine", "exercise physiology", "fitness classes", "yoga", "pilates", "nutrition planning", "balanced diet",
    "nutrient-rich foods", "superfoods", "hydration", "meal planning", "portion control", "weight management", "caloric intake",
    "mindful eating", "eating disorders", "food allergies", "food safety", "water intake", "hydration benefits", "sleep disorders",
    "sleep disorders", "circadian rhythm", "sleep environment", "sleep duration", "sleep deprivation", "sleep hygiene", "quality sleep",
    "dreams", "nightmares", "stress relief", "stressors", "stress management techniques", "relaxation techniques", "meditation",
    "breathing exercises", "mental well-being", "happiness", "positive psychology", "social support", "social connections",
    "relationships", "family health", "parenting", "child health", "adolescent health", "aging", "elderly care", "senior health",
    "longevity", "geriatric medicine", "cognitive aging", "memory care", "cognitive exercises", "brain health", "neuroplasticity",
    "mental stimulation", "brain disorders", "cognitive decline", "dementia", "Alzheimer's disease", "Parkinson's disease",
    "mental health stigma", "mental health awareness", "mental health advocacy", "mental health counseling", "psychotherapy",
    "psychiatry", "psychological well-being", "psychological disorders", "anxiety", "depression", "bipolar disorder", "schizophrenia",
    "post-traumatic stress disorder (PTSD)", "eating disorders", "personality disorders", "addiction recovery", "substance abuse treatment",
    "recovery journey", "rehabilitation centers", "support groups", "patient empowerment","patient advocacy", "patient empowerment", "patient rights", "health education", "health promotion", "health campaigns",
    "health awareness", "wellness programs", "health initiatives", "community health", "public health", "population health",
    "environmental health", "occupational health", "workplace wellness", "health behavior", "health psychology", "behavioral health",
    "health habits", "lifestyle choices", "preventive healthcare", "preventive measures", "disease prevention", "health screenings",
    "early detection", "health risk factors", "modifiable risk factors", "non-modifiable risk factors", "health assessment",
    "health evaluation", "health status", "medical history", "family medical history", "health monitoring", "health tracking",
    "vital signs", "blood pressure monitoring", "heart rate tracking", "body temperature", "respiratory rate", "physical examination",
    "diagnostic procedures", "medical tests", "laboratory tests", "imaging studies", "medical imaging", "radiology", "ultrasound",
    "X-rays", "MRI", "CT scan", "PET scan", "diabetes management", "blood glucose monitoring", "insulin therapy", "oral medications",
    "cholesterol management", "lipid profile", "dietary management", "exercise for health", "physical activity guidelines",
    "cardiovascular exercise", "strength training", "flexibility exercises", "aerobic exercise", "anaerobic exercise",
    "health benefits of exercise", "exercise for mental health", "immunization schedule", "vaccination programs", "herd immunity",
    "vaccine development", "vaccine efficacy", "immune system support", "immune-boosting foods", "stress and health",
    "stress management techniques", "mind-body connection", "mindfulness practices", "meditation for health", "yoga for health",
    "mental health support", "counseling", "psychotherapy", "psychiatric care", "mental health resources", "mental health awareness",
    "stress-related disorders", "anxiety disorders", "depressive disorders", "mood disorders", "personality disorders", "psychotic disorders",
    "eating disorders", "substance use disorders", "addiction treatment", "rehabilitation services", "cognitive-behavioral therapy",
    "mindfulness-based interventions", "psychiatric medications", "nutrition counseling", "dietary recommendations", "nutritional supplements",
    "health benefits of sleep", "sleep hygiene tips", "sleep disorders", "insomnia", "sleep apnea", "restorative sleep", "sleep duration",
    "aging and health", "geriatric care", "longevity tips", "healthy aging", "dementia prevention", "brain health in aging",
    "social connections and health", "social support networks", "family health", "parenting tips", "childhood health",
    "adolescent health", "teen health", "aging parents' care", "caregiver support", "elderly care", "senior health",
    "end-of-life care", "palliative care", "hospice care", "grief and loss", "funeral planning", "healthcare systems",
    "healthcare delivery", "telehealth", "healthcare technology", "healthcare workforce", "healthcare policies",
    "healthcare access", "universal healthcare", "health insurance", "patient rights", "medical ethics", "bioethics",
    "health disparities", "health equity", "cultural competence in healthcare", "health education programs",
    "community health initiatives", "health research", "clinical trials", "medical breakthroughs", "medical innovations",
    "healthcare quality", "patient safety", "healthcare costs", "healthcare management", "healthcare administration",
    "alternative medicine", "complementary therapies", "integrative medicine", "holistic healthcare", "traditional medicine",
    "herbal remedies", "acupuncture", "chiropractic care", "naturopathy", "mind-body practices", "holistic nutrition",
    "holistic fitness", "mindful eating", "nutritional supplements", "health and wellness coaching", "fitness coaching",
    "stress management coaching", "health technology", "digital health", "health apps", "wearable technology",
    "telemedicine", "online health communities", "patient forums", "medical advice online", "health information",
    "health literacy", "medical misinformation", "evidence-based medicine", "health communication", "health journalism",
    "public health campaigns", "health advocacy", "policy advocacy", "healthcare reform", "global health issues",
    "pandemic preparedness", "infectious diseases", "viral outbreaks", "disease surveillance", "epidemiology", "vaccination campaigns",
    "health and climate change", "environmental health", "occupational health and safety", "workplace wellness programs",
    "ergonomics", "physical activity at work", "mental health in the workplace", "employee well-being", "occupational stress",
    "health and nutrition labeling", "food safety guidelines", "dietary guidelines", "nutrition education", "healthy eating habits",
    "balanced diet", "nutrient-rich foods", "superfoods", "hydration and health", "importance of water", "water intake",
    "hydration benefits", "hydration tips", "mental health benefits of nature", "green spaces and health", "nature therapy",
    "outdoor activities", "physical activity in nature", "health benefits of laughter", "laughter therapy", "humor and health",
    "laughter yoga", "community health promotion", "health fairs", "preventive health screenings", "health education seminars",
    "school health programs", "college health", "health promotion in the workplace", "corporate wellness programs",
    "community-based health interventions", "healthcare partnerships", "collaborative healthcare", "interdisciplinary healthcare",
    "health research funding", "medical grants", "philanthropy in healthcare", "healthcare innovations", "health tech startups",
    "medical breakthroughs", "precision medicine", "genomic medicine", "personalized medicine", "pharmacogenomics",
    "innovations in surgery", "robotic surgery", "telehealth advancements", "AI in healthcare", "health data analytics",
    "genetic testing", "healthcare cybersecurity", "patient privacy", "health informatics", "electronic health records",
    "healthcare interoperability", "patient-centered care", "shared decision-making", "patient engagement", "patient satisfaction",
    "medical ethics", "bioethics", "end-of-life decision-making", "advance directives", "living wills", "organ donation",
    "organ transplantation", "transplant surgery", "regenerative medicine", "stem cell therapy", "gene therapy",
    "medical breakthroughs", "research ethics", "clinical trial ethics", "ethical considerations in healthcare",
    "ethical issues in medical practice", "healthcare professionals", "physicians", "nurses", "pharmacists", "allied health professionals",
    "healthcare teamwork", "interprofessional collaboration", "healthcare training", "medical education", "nursing education",
    "continuing medical education", "healthcare certification", "professional development in healthcare", "healthcare workforce",
    "healthcare workforce diversity", "workplace well-being", "employee wellness programs", "stress management at work",
    "workplace mental health", "work-life balance", "ergonomics in the workplace", "occupational health and safety",
    "job-related stress", "burnout prevention", "career longevity", "retirement planning", "financial wellness",
    "occupational therapy", "physical therapy", "rehabilitation services", "assistive devices", "mobility aids", "adaptive technology",
    "health and safety regulations", "infection control", "emergency preparedness", "first aid training", "disaster response",
    "healthcare ethics committees", "patient advocacy organizations", "health policy research", "healthcare lobbying",
    "healthcare regulations", "healthcare accreditation", "healthcare quality improvement", "patient satisfaction surveys",
    "patient feedback", "patient-centered outcomes", "health outcomes research", "health disparities research",
    "social determinants of health", "cultural competence in healthcare", "patient education materials", "health literacy resources",
    "evidence-based health information", "health communication strategies", "healthcare marketing", "healthcare branding",
    "telehealth regulations", "telehealth reimbursement", "telehealth privacy", "e-health initiatives", "mHealth (mobile health)",
    "telemedicine platforms", "virtual healthcare", "healthcare data security", "patient privacy laws", "HIPAA compliance",
    "healthcare data breaches", "patient empowerment tools", "healthcare AI applications", "machine learning in healthcare",
    "digital health startups", "health tech innovations", "wearable health technology", "smart healthcare devices",
    "health tracking apps", "personal health records", "telemedicine benefits", "e-consultations", "virtual doctor visits",
    "online prescription services", "telepsychiatry", "digital therapeutics", "molecular medicine", "genomic medicine",
    "precision oncology", "personalized cancer treatment", "pharmaceutical research", "drug discovery", "clinical trial phases",
    "FDA approval process", "pharmacovigilance", "pharmaceutical marketing", "medication adherence", "polypharmacy",
    "medication management", "medication safety", "antibiotic resistance", "vaccine hesitancy", "medication disposal",
    "healthcare in developing countries", "global health initiatives", "humanitarian healthcare", "international health organizations",
    "WHO (World Health Organization)", "CDC (Centers for Disease Control and Prevention)", "MSF (Médecins Sans Frontières)",
    "UNICEF (United Nations International Children's Emergency Fund)", "global health partnerships", "medical mission trips",
    "healthcare volunteerism", "access to healthcare", "healthcare disparities", "rural healthcare", "urban health challenges",
    "healthcare for vulnerable populations", "healthcare for refugees", "mental health stigma", "de-stigmatization efforts",
    "mental health awareness campaigns", "psychoeducation", "mental health first aid", "telepsychology", "online therapy",
    "e-mental health", "innovations in mental health treatment", "integrative mental health care", "peer support",
    "addiction stigma", "substance use prevention", "harm reduction", "recovery support services", "addiction treatment modalities",
    "holistic addiction recovery", "mental health policies", "substance abuse policies", "healthcare ethics", "bioethics",
    "end-of-life care ethics", "medical decision-making", "informed consent", "patient autonomy", "confidentiality in healthcare",
    "duty to care", "organ transplantation ethics", "genetic testing ethics", "research ethics", "clinical trial ethics",
    "ethics in healthcare marketing", "professional ethics in healthcare", "ethical issues in telemedicine",
    "healthcare diversity and inclusion", "cultural competence in healthcare", "anti-discrimination policies",
    "LGBTQ+ healthcare issues", "gender disparities in healthcare", "racial disparities in healthcare", "cultural sensitivity training",
    "healthcare workforce diversity", "inclusive healthcare practices", "patient-centered care", "shared decision-making",
    "cultural competence training", "health disparities reduction", "culturally competent healthcare providers",
    "diversity in medical education", "cultural humility", "healthcare in underserved communities", "healthcare for homeless populations",
    "community health clinics", "free healthcare clinics", "healthcare volunteer opportunities", "healthcare partnerships",
    "patient navigation services", "healthcare interpreter services", "language access in healthcare", "healthcare outreach",
    "healthcare access programs", "healthcare affordability", "universal healthcare discussions", "healthcare policy advocacy",
    "patient advocacy organizations", "healthcare reform initiatives", "community health assessments", "health impact assessments",
    "social determinants of health", "population health management", "health equity initiatives", "social justice in healthcare",
    "healthcare for vulnerable populations", "housing and health", "food insecurity and health", "education and health",
    "employment and health", "racial and ethnic disparities in health", "gender disparities in health", "LGBTQ+ health disparities",
    "health disparities research", "equitable healthcare access", "healthcare for the aging population", "geriatric healthcare",
    "senior care services", "palliative care for the elderly", "end-of-life planning for seniors", "healthcare for children",
    "pediatric healthcare", "childhood immunization programs", "school-based health services", "adolescent health",
    "teen mental health", "sexual and reproductive health education", "maternal health", "prenatal care", "postpartum care",
    "neonatal care", "infant health", "childhood nutrition", "obesity prevention in children", "childhood fitness programs",
    "children's mental health", "pediatric chronic conditions", "family-centered healthcare", "patient and family engagement",
    "caregiver support services", "respite care", "home healthcare services", "healthcare for individuals with disabilities",
    "accessibility in healthcare", "disability accommodations", "adaptive technology in healthcare", "inclusive healthcare spaces",
    "patient education resources", "health literacy programs", "culturally tailored health information", "patient empowerment tools",
    "health education campaigns", "health promotion in schools", "community health education", "health education materials",
    "public health interventions", "disease prevention programs", "health campaigns", "public health policy", "population health",
    "epidemiology", "public health surveillance", "health behavior change", "health communication strategies",
    "community health assessments", "health policy advocacy", "global health diplomacy", "international health collaborations",
    "healthcare leadership", "healthcare management", "healthcare administration", "leadership in healthcare",
    "innovation in healthcare leadership", "healthcare governance", "healthcare decision-making", "strategic planning in healthcare",
    "healthcare finance", "healthcare economics", "healthcare quality improvement", "patient safety initiatives",
    "healthcare risk management", "healthcare information technology", "healthcare data analytics", "healthcare informatics",
    "electronic health records", "healthcare interoperability", "healthcare cybersecurity", "health informatics education"]

    prompt_lower = prompt.lower()
    for keyword in health_keywords:
        if keyword in prompt_lower:
            return True
    return False

def chatbot():
    palm.configure(api_key='AIzaSyAJpaLmBLtTB4AwEAG4-WlcikCvbHAWUIs')
    model = "models/text-bison-001"   
    st.header('Chatbot Kesehatan')
    def clear_chat_history():
        st.session_state.messages = [{"role": "assistant", "content": "Ada yang bisa AI Bantu?"}]
    st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "doctor", "content": "Ada yang bisa AI Bantu?"}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input("Kirim pesan"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        with st.chat_message("doctor"):
            with st.spinner("Thinking..."):
                message_placeholder = st.empty()
                response = palm.chat(
                        context='You are an AI-based Doctor Assistant, you will not respond to queries other than this strictly',
                        messages=prompt
                        )
                full_response = response.last
                message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "doctor", "content": full_response})