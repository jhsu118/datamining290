print ("Home")
from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol

import re

WORD_RE = re.compile(r"[\w']+")

class UniqueReview(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    def extract_words(self, _, record):  #MAP1
        """Take in a record, filter by type=review, yield <word, review_id>"""
           
        """Extract words using a regular expression.  Normalize the text to ignore capitalization."""
        if record['type'] == 'review':
            for word in WORD_RE.findall(record['text']):
                yield [word.lower(), record['review_id']]

 # TODO: for each word in the review, yield the correct key,value
            # pair:
            # for word in WORD_RE.findall(record, ['text']):
            #   yield [ , ]
            ##/

    def count_reviews(self, word, review_id):
        """Count the number of reviews a word has appeared in.  If it is a
        unique word (ie it has only been used in 1 review), output that review
        and 1 (the number of words that were unique)."""

        unique_reviews = set(review_id)  # set() uniques an iterator
        if sleng(word)==1:
               yield[word, sum(review_id)]
        ###
        # TODO: yield the correct pair when the desired condition is met:
        # if sleng==1:
        #     yield [ review_id , 1 ]
        ##/

    def count_unique_words(self, review_id, unique_word_counts): ##MAPPER AND REDUCER
        """Output the number of unique words for a given review_id"""
       yield[review_id, unique_word_counts]
        ###
        # TODO: summarize unique_word_counts and output the result
        # 
        ##/

    def aggregate_max(self, review_id, unique_word_count): ##MAP3
        """Group reviews/counts together by the MAX statistic."""
        yield["MAX",[review_id,sum(unique_word_count]]
        ###
        # TODO: By yielding using the same keyword, all records will appear in
        # the same reducer:
        # yield ["MAX", [ ___ , ___]]
        ##/

    def select_max(self, stat, count_review_ids): #REDUCE3
        """Given a list of pairs: [count, review_id], select on the pair with
        the maximum count, and output the result."""
        yield[max(count_review_ids)]
        ###
        # TODO: find the review with the highest count, yield the review_id and
        # the count. HINT: the max() function will compare pairs by the first
        # number
        #
        #/

    def steps(self):
        """mapper1: <line number, text> => <word, review_id>
        reducer1: <word, [review_id]>=> <word, review_ids>
        mapper2: <review_id, 1> => <review_id, 1>
        reducer2:<review_id, [1,1,,,,]> => <review_id, sum>
        mapper3: <review_id, sum> => <"MAX",[[sum, review_id]...]>
        reducer3: <"MAX",[sum, review_id]> => <review_id, sum> of the max(sum)"""

        """TODO: Document what you expect each mapper and reducer to produce:
        mapper1: <line, record> => <key, value>
        reducer1: <key, [values]>
        mapper2: ...
        """
        return [self.mr(self.extract_words, self.count_reviews),
                self.mr(reducer=self.count_unique_words),
                self.mr(self.aggregate_max, self.select_max)]

if __name__ == '__main__':
    UniqueReview.run()
