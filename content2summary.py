from pelican import signals
from bs4 import BeautifulSoup


def content2summary(generator):
    max_length = generator.settings.get('SUMMARY_MAX_LENGTH')

    for article in generator.articles:
        if 'summary' not in article.metadata.keys():
            summary = ' '.join(article.content.split()[:max_length]) + ' ...'
            soup = BeautifulSoup(summary, "html.parser")
            article.metadata['summary'] = soup.get_text()


def register():
    """ Register plugin """
    signals.article_generator_finalized.connect(content2summary)
