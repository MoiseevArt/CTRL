CTRL
-

Classification of the tonality of the Russian language.
-
Проект "CTRL" представляет собой рекуррентную нейронную сеть (RNN), разработанную для анализа тональности предложений на русском языке. Модель предназначена для определения настроений текстов и классифицирует их на два класса: негативный и положительный.

"CTRL" - это NLP модель, обученная на наборе данных, содержащем более 2 миллионов отзывов пользователей Amazon. Этот набор данных обеспечивает широкий охват различных стилей и тематик текстов, что позволяет модели определять тональность с точностью более 90%.

Метод tonality() является основным инструментом для анализа тональности текста. Он принимает на вход текст и возвращает массив, содержащий два значения: вероятность принадлежности текста к классу негативных настроений и вероятность отнесения к классу положительных настроений.

Все необходимые зависимости находятся в requirements.txt


Classification of the tonality of the Russian language.
-
The "CTRL" project is a recurrent neural network (RNN) designed to analyze the sentiment of Russian language sentences. The model is intended to determine the mood of texts and classify them into two categories: negative and positive.

"CTRL" is an NLP model trained on a dataset containing over 2 million Amazon user reviews. This dataset covers a wide range of styles and themes, enabling the model to accurately determine sentiment with over 90% accuracy.

The tonality() method is the primary tool for analyzing text sentiment. It takes text as input and returns an array containing two values: the probability of the text belonging to the negative sentiment class and the probability of belonging to the positive sentiment class.

All necessary dependencies are listed in requirements.txt
