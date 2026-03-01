def response(hey_bob):
    response = ''

    if hey_bob.isupper() and not hey_bob.islower() and len(hey_bob.strip()) > 0:
        if hey_bob.rstrip().endswith("?"):
            response = "Calm down, I know what I'm doing!"
        else:
            response = "Whoa, chill out!"
    elif hey_bob.rstrip().endswith("?"):
        response = "Sure."
    elif len(hey_bob.strip()) == 0:
        response = "Fine. Be that way!"
    else:
        response = "Whatever."

    return response
