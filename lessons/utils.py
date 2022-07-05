from django.template.defaultfilters import slugify


def get_lesson_file(instance, filename):
    title = instance.topic.topic_name
    slug = slugify(title)
    return "lesson_images/%s-%s" % (slug, filename) # TODO validate videos or images
