def star_rating(rating):
    stars = []

    f = float(rating)
    x = int(f)
    for number in range(0, x):
        stars.append("fas fa-star")

    dec = f - x
    if dec > .74:
        stars.append("fas fa-star")
    if dec >= .26 and dec < .75:
        stars.append("fas fa-star-half-alt")
    elif dec > 0:
        stars.append("far fa-star")

    last = int(5 - f)
    for number in range(0, last):
        stars.append("far fa-star")

    return stars
