def route_question(question):

    question = question.lower()

    if any(word in question for word in [
        "flood",
        "rain",
        "water"
    ]):
        return "disaster"

    elif any(word in question for word in [
        "climate",
        "temperature",
        "global warming"
    ]):
        return "climate"

    elif any(word in question for word in [
        "safety",
        "emergency",
        "warning"
    ]):
        return "safety"

    else:
        return "general"


if __name__ == "__main__":

    q = "What should I do during a flood?"

    print(route_question(q))