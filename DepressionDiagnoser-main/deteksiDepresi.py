# expert_system_backend.py
class MentalHealthExpertSystem:
    def __init__(self):
        # Initialize the knowledge base
        self.diseases = {
            'P1': {'name': 'Depresi', 'symptoms': ['G3', 'G5', 'G10', 'G13', 'G16', 'G17', 'G21', 'G24', 'G26', 'G31', 'G34', 'G37', 'G38', 'G42']},
            'P2': {'name': 'Kecemasan', 'symptoms': ['G2', 'G4', 'G7', 'G9', 'G15', 'G19', 'G20', 'G23', 'G25', 'G28', 'G30', 'G36', 'G40', 'G41']},
            'P3': {'name': 'Stres', 'symptoms': ['G1', 'G6', 'G8', 'G11', 'G12', 'G14', 'G18', 'G22', 'G27', 'G29', 'G32', 'G33', 'G35', 'G39']}
        }
        
        self.symptoms = {
            'G1': 'Saya merasa mudah marah karena hal-hal kecil',
            'G2': 'Saya merasa bibir terasa kering',
            'G3': 'Saya tidak dapat merasakan perasaan yang positif atau baik',
            'G4': 'Saya merasakan kesulitan dalam bernafas seperti terengah-engah atau sesak nafas padahal tidak sedang melakukan kegiatan fisik sebelumnya',
            'G5': 'Saya merasa seperti tidak bertenaga dalam melakukan kegiatan',
            'G6': 'Saya merasa cenderung bereaksi berlebihan pada suatu keadaan',
            'G7': 'Saya merasa goyah seperti kaki terasa pegal',
            'G8': 'Saya merasa sulit untuk bersantai',
            'G9': 'Ketika pada situasi tertentu saya merasakan cemas yang berlebihan tetapi jika situasi tersebut berakhir saya merasa sangat lega',
            'G10': 'Saya merasa tidak ada hal yang dapat diharapkan di masa depan',
            'G11': 'Saya mudah merasa kesal',
            'G12': 'Saya merasa kehabisan energi karena merasa cemas',
            'G13': 'Saya merasa sedih dan tertekan',
            'G14': 'Saya merasa diri saya menjadi tidak sabaran dalam situasi tertentu seperti saat menunggu sesuatu',
            'G15': 'Saya merasa bahwa diri saya lemas seperti mau pingsan',
            'G16': 'Saya merasa diri saya kehilangan minat akan segala hal',
            'G17': 'Saya merasa diri saya tidak layak',
            'G18': 'Saya merasa saya mudah tersinggung',
            'G19': 'Saya berkeringat berlebihan seperti tangan berkeringat padahal suhu tidak panas dan tidak sedang melakukan fisik sebelumnya',
            'G20': 'Saya merasa merasa takut tanpa alasan yang jelas',
            'G21': 'Saya merasa hidup tidak bermanfaat',
            'G22': 'Saya merasa sulit untuk beristirahat',
            'G23': 'Saya mengalami kesulitan dalam menelan',
            'G24': 'Saya merasa tidak dapat menikmati hal-hal yang saya lakukan',
            'G25': 'Saya merasakan perubahan pada kegiatan jantung atau denyut nadi padahal saya tidak melakukan latihan fisik',
            'G26': 'Saya merasa kehilangan harapan dan putus asa',
            'G27': 'Saya merasakan bahwa diri saya mudah marah',
            'G28': 'Saya merasa saya mudah panik',
            'G29': 'Saya merasa susah untuk tenang setelah ada sesuatu hal yang mengganggu saya',
            'G30': 'Saya merasa takut kalau saya akan terhambat oleh tugas-tugas sepele yang tidak biasa saya lakukan',
            'G31': 'Saya merasa kesulitan untuk antusias dengan banyak hal',
            'G32': 'Saya susah untuk sabar dalam menghadapi gangguan terhadap hal yang sedang saya lakukan',
            'G33': 'Saya sedang merasa gelisah',
            'G34': 'Saya merasa bahwa diri saya tidak berguna',
            'G35': 'Saya tidak bisa memaklumi hal apapun yang menghalangi saya dalam menyelesaikan hal yang sedang saya lakukan',
            'G36': 'Saya merasa takut berlebihan pada beberapa situasi tertentu',
            'G37': 'Saya tidak melihat adanya impian untuk masa depan',
            'G38': 'Saya merasa hidup saya tidak berarti',
            'G39': 'Saya merasa diri saya mudah bimbang',
            'G40': 'Saya merasa khawatir dengan situasi dimana saya mungkin menjadi panik dan mempermalukan diri sendiri',
            'G41': 'Saya merasa gemetar seperti gemetar pada tangan',
            'G42': 'Saya merasa susah untuk meningkatkan inisiatif dalam melakukan sesuatu'
        }
        
        # Severity levels for each condition
        self.severity_levels = {
            'P1': {  # Depression
                'Normal': (0, 9),
                'Ringan': (10, 13),
                'Sedang': (14, 20),
                'Berat': (21, 27)
            },
            'P2': {  # Anxiety
                'Normal': (0, 7),
                'Ringan': (8, 9),
                'Sedang': (10, 14),
                'Berat': (15, 19)
            },
            'P3': {  # Stress
                'Normal': (0, 14),
                'Ringan': (15, 18),
                'Sedang': (19, 25),
                'Berat': (26, 33)
            }
        }
        
        # Solutions/recommendations for each condition and severity
        self.recommendations = {
            'P1': {
                'Normal': "Kondisi mental Anda dalam keadaan normal. Tetap jaga pola hidup sehat dan hubungan sosial yang baik.",
                'Ringan': "Anda menunjukkan beberapa gejala depresi ringan. Cobalah untuk lebih sering beraktivitas fisik, tidur cukup, dan berbicara dengan orang yang Anda percayai.",
                'Sedang': "Anda menunjukkan gejala depresi sedang. Pertimbangkan untuk mencari bantuan profesional seperti psikolog atau konselor. Jaga rutinitas harian dan hindari isolasi sosial.",
                'Berat': "Anda menunjukkan gejala depresi berat. Sangat disarankan untuk segera berkonsultasi dengan psikolog atau psikiater. Jangan ragu untuk mencari bantuan dari orang terdekat."
            },
            'P2': {
                'Normal': "Tingkat kecemasan Anda dalam batas normal. Teruslah mengelola stres dengan baik.",
                'Ringan': "Anda mengalami kecemasan ringan. Cobalah teknik relaksasi seperti pernapasan dalam atau meditasi untuk membantu mengelola kecemasan.",
                'Sedang': "Anda mengalami kecemasan sedang. Pertimbangkan untuk mempelajari teknik manajemen kecemasan atau mencari bantuan profesional jika gejala mengganggu kehidupan sehari-hari.",
                'Berat': "Anda mengalami kecemasan berat. Sangat disarankan untuk segera berkonsultasi dengan profesional kesehatan mental. Kecemasan berat dapat dikelola dengan terapi yang tepat."
            },
            'P3': {
                'Normal': "Tingkat stres Anda dalam batas normal. Teruslah menjaga keseimbangan hidup.",
                'Ringan': "Anda mengalami stres ringan. Cobalah teknik manajemen waktu dan relaksasi untuk mengurangi beban stres.",
                'Sedang': "Anda mengalami stres sedang. Identifikasi sumber stres dan cari cara untuk menguranginya. Pertimbangkan untuk mencari dukungan sosial atau profesional.",
                'Berat': "Anda mengalami stres berat. Stres tingkat ini dapat mempengaruhi kesehatan fisik dan mental. Sangat disarankan untuk mencari bantuan profesional dan mengurangi beban stres segera."
            }
        }

    def backward_chaining(self, user_responses):
        """
        Perform backward chaining to determine the mental health condition
        based on user responses to symptoms.
        
        Args:
            user_responses: Dictionary of {symptom_code: weight} where weight is 0-3
            
        Returns:
            Dictionary containing diagnosis results for each condition
        """
        results = {}
        
        # Calculate total scores for each condition
        for disease_code, disease_info in self.diseases.items():
            total_score = 0
            matched_symptoms = []
            
            for symptom_code in disease_info['symptoms']:
                if symptom_code in user_responses:
                    total_score += user_responses[symptom_code]
                    matched_symptoms.append(symptom_code)
            
            # Determine severity level
            severity = self.determine_severity(disease_code, total_score)
            
            results[disease_code] = {
                'name': disease_info['name'],
                'score': total_score,
                'severity': severity,
                'matched_symptoms': matched_symptoms,
                'recommendation': self.recommendations[disease_code][severity]
            }
        
        return results
    
    def determine_severity(self, disease_code, score):
        """
        Determine the severity level based on the score for a given condition.
        """
        levels = self.severity_levels[disease_code]
        
        for level, (min_score, max_score) in levels.items():
            if min_score <= score <= max_score:
                return level
        
        # If score is above the highest range, return the highest severity
        return 'Berat'
    
    def get_all_symptoms(self):
        """
        Return all symptoms with their codes and descriptions.
        """
        return self.symptoms
    
    def get_symptom_description(self, symptom_code):
        """
        Get the description for a specific symptom code.
        """
        return self.symptoms.get(symptom_code, "Unknown symptom")