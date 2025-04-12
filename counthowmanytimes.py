def count_good():
    feedback = input("Enter your feedback: ")
    feedback_lower = feedback.lower()
    good_count = feedback_lower.count("good")

    print(f" The word 'good' appears {good_count} time(s) in the feedback.")

count_good()
