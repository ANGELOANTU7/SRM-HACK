# LearnMateAI
TRACK - AI/ML
LearnMateAI is an AI/ML-powered learning platform that aims to revolutionize traditional learning methods by providing a personalized and adaptive learning experience to students. It adapts to the student's learning pace and style, focuses on important topics, and offers instant feedback through regular testing.

### Working Screenshots

| <img src="gifs/1.gif">             | <img src="gifs/2.gif">              | 
| :----------------------------------: | :------------------------------------: |
|          _Website(React+TailWind)_           |      _Lecture Handwritten/PDF to text (Goggle_vison_API)_          | 

| <img src="gifs/3.gif">             | <img src="gifs/4.gif">              | 
| :----------------------------------: | :------------------------------------: |
|          _Notes summarizer using Hugging Face pipeline_           |      _Question,Important topic gen using OpenAI_          | 

| <img src="gifs/5.gif">             | <img src="gifs/6.gif">              | 
| :----------------------------------: | :------------------------------------: |
|          _AI tutor chatting trained using Notes and PYQs_           |      _Study planner_          | 
## Key Features

- Personalized AI tutor: LearnMateAI acts as a virtual tutor, leveraging artificial intelligence and machine learning algorithms to deliver tailored educational content based on the student's individual needs.
- Intelligent topic selection: The system learns subject areas from teacher's notes and previous year's question papers to identify important topics that require focus.
- Step-by-step learning: LearnMateAI guides students through the learning process, providing comprehensive explanations and examples for each topic, ensuring a thorough understanding.
- Adaptive learning curve: The system adapts to the student's learning curve, adjusting the difficulty level and pace of the lessons to maximize comprehension and retention.
- Instant feedback and testing: Regular testing and assessments enable LearnMateAI to provide immediate feedback, helping students identify areas that need improvement and reinforcing learning outcomes.
- Imp topics and question paper generation: LearnMateAI generates important topics and possible question papers, assisting students in their exam preparations.
- Engaging learning experience: LearnMateAI interacts with students like an AI tutor, offering an engaging and interactive learning environment.

## Challenges and Solutions

During the development of LearnMateAI, we encountered some challenges that required us to adapt our deployment strategy and optimize the performance of the system.

1. Deployment Limitations: Initially, we faced limitations with AWS Lambda regarding package imports, specifically due to the maximum package size limit of 250 MB. To overcome this, we attempted to integrate AWS containers with AWS Lambda, but we also encountered policy limitations. As a result, we decided to deploy the system locally instead.

2. Processing Time: TensorFlow, a crucial component of our system, was taking longer than expected to process data. To address this issue, we leveraged the Intel One API optimization tool (DNN), which significantly enhanced TensorFlow's performance and reduced processing time.

Through careful troubleshooting and finding alternative solutions, we successfully resolved these challenges and continued building the LearnMateAI project.

## Getting Started

To get started with LearnMateAI, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/LearnMateAI.git`
2. Install the necessary dependencies: `pip install -r requirements.txt`
3. Configure the system settings and parameters according to your requirements.
4. Run the application: `python app.py`
5. Access LearnMateAI through your preferred web browser at `http://localhost:5000`.

## Contributions

Contributions to LearnMateAI are welcome! If you find any issues or have suggestions for improvement, please submit a pull request or open an issue on the repository.

## License

This project is licensed under the MIT License. Feel free to modify and distribute the code as per the license terms.

## Acknowledgments

We would like to acknowledge the contributions of the team members and the support received during the development of LearnMateAI.

**Note:** The project gif is for illustration purposes only and does not reflect the actual user interface or functionality of LearnMateAI.
