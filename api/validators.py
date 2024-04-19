MOVIE_FIELDS = ['title', 'original_title', 'release_date',
                'play_time', 'rating', 'max_rating', 'short_story', 'genre']


def validate_movie_data(data):
    validated_data = {}
    for k, v in data.items():
        if k in MOVIE_FIELDS:
            validated_data[k] = v

    return validated_data


def validate_movie_query(args_from_request):
    validated_query = {}
    for arg in MOVIE_FIELDS:
        if arg in args_from_request:
            validated_query[arg] = args_from_request.get(arg)

    return validated_query


def validate_id(entity_id):
    if entity_id.isnumeric():
        return int(entity_id)

    return None
