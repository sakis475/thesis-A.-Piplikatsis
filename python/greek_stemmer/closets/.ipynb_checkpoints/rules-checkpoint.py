# -*- coding: utf-8 -*-

# extracted rules for stemming

rules = {
    'verbs': {
        'irregular': {
            'type_1': ['ΕΙΜΑΙ', 'ΕΙΣΑΙ', 'ΕΙΝΑΙ', 'ΕΙΜΑΣΤΕ', 'ΕΙΣΤΕ', 'ΕΙΣΑΣΤΕ'],
            'type_2': ['ΗΜΟΥΝ', 'ΗΣΟΥΝ', 'ΗΤΑΝΕ', 'ΗΜΟΥΝΑ', 'ΗΣΟΥΝΑ', 'ΗΜΑΣΤΕ', 'ΗΣΑΣΤΕ', 'ΗΜΑΣΤΑΝ', 'ΗΣΑΣΤΑΝ', 'ΗΤΑΝ',
                       'ΔΩ', 'ΔΕΙΣ', 'ΔΕΙ', 'ΔΟΥΜΕ', 'ΔΕΙΤΕ', 'ΔΟΥΝ', 'ΠΩ', 'ΠΕΙΣ', 'ΠΕΙ', 'ΠΟΥΜΕ', 'ΠΕΙΤΕ', 'ΠΟΥΝ',
                       'ΖΩ', 'ΖΕΙΣ', 'ΖΕΙ', 'ΖΟΥΜΕ', 'ΖΕΙΤΕ', 'ΖΟΥΝ', 'ΖΟΥΝΕ', 'ΖΟΥΣΑ', 'ΖΟΥΣΕΣ', 'ΖΟΥΣΕ', 'ΖΟΥΣΑΜΕ',
                       'ΖΟΥΣΑΤΕ', 'ΖΟΥΣΑΝΕ', 'ΖΟΥΣΑΝ']
        },
        'singular': ['ΙΟΜΟΥΝΑ', 'ΙΟΣΟΥΝΑ', 'ΟΥΜΟΥΝΑ', 'ΟΥΣΟΥΝΑ', 'ΙΟΜΟΥΝ', 'ΙΟΣΟΥΝ', 'ΙΟΤΑΝΕ', 'ΟΥΣΟΥΝ', 'ΟΥΜΟΥΝ',
                     'ΟΜΟΥΝΑ', 'ΟΣΟΥΝΑ', 'ΑΡΗΣΕΣ', 'ΩΝΤΑΣ', 'ΟΝΤΑΣ', 'ΟΜΟΥΝ', 'ΟΣΟΥΝ', 'ΟΤΑΝΕ', 'ΟΥΣΑΙ', 'ΟΥΤΑΙ',
                     'ΟΥΣΕΣ', 'ΑΡΕΙΣ', 'ΙΕΜΑΙ', 'ΙΕΣΑΙ', 'ΙΕΤΑΙ', 'ΟΥΜΑΙ', 'ΕΙΣΑΙ', 'ΕΙΤΑΙ', 'ΙΟΤΑΝ', 'ΑΡΗΣΕ', 'ΑΡΗΣΑ',
                     'ΕΣΑΙ', 'ΕΤΑΙ', 'ΗΚΕΣ', 'ΟΜΑΙ', 'ΟΤΑΝ', 'ΟΥΣΑ', 'ΟΥΣΕ', 'ΑΓΕΣ', 'ΩΜΑΙ', 'ΑΣΑΙ', 'ΑΤΑΙ', 'ΑΡΕΣ',
                     'ΑΡΕΙ', 'ΜΑΙ', 'ΣΑΙ', 'ΤΑΙ', 'ΜΗΝ', 'ΗΚΑ', 'ΗΚΕ', 'ΕΙΣ', 'ΑΕΙ', 'ΑΓΑ', 'ΑΓΕ', 'ΟΙΣ', 'ΑΡΩ', 'ΑΡΑ',
                     'ΑΡΕ', 'ΟΥ', 'ΗΝ', 'ΗΣ', 'ΕΙ', 'ΑΩ', 'ΑΣ', 'ΕΣ', 'ΟΙ', 'ΣΟ', 'ΤΟ', 'Ω', 'Α', 'Ε', 'Η'],

        'plural': ['ΙΟΝΤΟΥΣΑΝ', 'ΙΟΜΑΣΤΑΝ', 'ΙΟΣΑΣΤΑΝ', 'ΙΟΥΝΤΑΝΕ', 'ΟΥΜΑΣΤΑΝ', 'ΟΥΣΑΣΤΑΝ', 'ΟΝΤΟΥΣΑΝ', 'ΟΜΑΣΤΑΝ',
                   'ΟΥΝΤΑΝΕ', 'ΟΣΑΣΤΑΝ', 'ΑΡΗΣΑΜΕ', 'ΑΡΗΣΑΤΕ', 'ΙΟΜΑΣΤΕ', 'ΙΟΣΑΣΤΕ', 'ΙΟΥΝΤΑΙ', 'ΟΥΜΑΣΤΕ', 'ΙΟΝΤΑΝΕ',
                   'ΙΟΥΝΤΑΝ', 'ΑΓΑΜΕ', 'ΑΓΑΤΕ', 'ΟΥΣΘΕ', 'ΩΜΕΘΑ', 'ΑΡΕΤΕ', 'ΑΡΟΥΝ', 'ΩΝΤΑΣ', 'ΩΝΤΑΙ', 'ΑΡΑΜΕ', 'ΑΡΑΤΕ',
                   'ΑΡΑΝΕ', 'ΟΝΤΑΣ', 'ΗΚΑΜΕ', 'ΕΙΣΤΕ', 'ΟΝΤΑΙ', 'ΗΚΑΤΕ', 'ΗΚΑΝΕ', 'ΑΓΑΝΕ', 'ΟΝΤΑΝ', 'ΙΕΣΤΕ', 'ΟΥΤΑΝ',
                   'ΟΥΣΙΝ', 'ΟΥΣΑΝ', 'ΟΥΤΕ', 'ΜΕΘΑ', 'ΝΤΑΙ', 'ΗΜΕΝ', 'ΗΣΕΝ', 'ΗΣΑΝ', 'ΗΚΑΝ', 'ΟΥΜΕ', 'ΟΥΝΕ', 'ΕΙΤΕ',
                   'ΑΣΘΕ', 'ΑΓΑΝ', 'ΕΣΤΕ', 'ΑΡΑΝ', 'ΩΜΕΝ', 'ΟΥΣΙ', 'ΟΜΕ', 'ΕΤΕ', 'ΑΜΕ', 'ΑΤΕ', 'ΑΝΕ', 'ΟΥΝ', 'ΗΤΕ',
                   'ΣΘΕ', 'ΝΤΟ', 'ΑΝ', 'ΤΕ']
    },

    'non_verbs': {
        'neuter_noun': {
            'matos': ['ΜΑΤΟΣ', 'ΜΑΤΩΝ', 'ΜΑΤΑ', 'ΜΑ']
        },
        'propername': ['ΟΝΟΣ', 'ΩΝΟΣ', 'ΟΡΟΣ', 'ΕΥΣ', 'ΕΩΣ', 'ΟΝΤΟΣ', 'ΚΤΟΣ', 'ΟΥΣ', 'ΩΝ', 'ΩΡ', 'ΙΣ', 'ΩΣ', 'Ξ', 'Ω'],
        
        'adjectives': ['ΟΥΣΤΕΡΟΥΣ', 'ΟΥΣΤΑΤΟΥΣ', 'ΟΥΣΤΕΡΟΥ', 'ΟΥΣΤΕΡΟΣ', 'ΕΣΤΕΡΟΥΣ', 'ΟΥΣΤΕΡΗΣ', 'ΕΣΤΑΤΟΥΣ', 'ΟΥΣΤΕΡΩΝ',
                       'ΟΥΣΤΑΤΕΣ', 'ΟΥΣΤΕΡΕΣ', 'ΟΥΣΤΕΡΟΙ', 'ΑΙΤΕΡΟΥΣ', 'ΟΥΣΤΑΤΟΣ', 'ΟΥΣΤΑΤΟΥ', 'ΟΥΣΤΑΤΗΣ', 'ΟΥΣΤΑΤΩΝ',
                       'ΥΤΕΡΟΥΣ', 'ΕΣΤΕΡΟΙ', 'ΕΣΤΕΡΩΝ', 'ΕΣΤΕΡΕΣ', 'ΟΥΣΤΕΡΗ', 'ΩΜΕΝΟΥΣ', 'ΕΣΤΑΤΗΣ', 'ΕΣΤΕΡΑΣ',
                       'ΕΣΤΕΡΗΣ', 'ΟΥΣΤΕΡΟ', 'ΑΣΜΕΝΟΙ', 'ΟΤΕΡΟΥΣ', 'ΕΣΤΑΤΟΥ', 'ΕΣΤΑΤΟΣ', 'ΟΥΣΤΕΡΑ', 'ΕΣΤΑΤΕΣ',
                       'ΥΤΑΤΟΥΣ', 'ΕΣΤΕΡΟΥ', 'ΕΣΤΕΡΟΣ', 'ΑΙΤΕΡΟΣ', 'ΑΙΤΕΡΟΥ', 'ΕΣΤΑΤΟΙ', 'ΑΙΤΕΡΟΙ', 'ΑΙΤΕΡΩΝ',
                       'ΑΙΤΕΡΗΣ', 'ΑΙΤΕΡΑΣ', 'ΟΥΜΕΝΟΥ', 'ΟΥΜΕΝΟΣ', 'ΟΥΜΕΝΗΣ', 'ΟΥΜΕΝΩΝ', 'ΟΥΜΕΝΕΣ', 'ΟΜΕΝΟΥΣ',
                       'ΕΣΤΑΤΩΝ', 'ΕΣΤΕΡΟΝ', 'ΗΜΕΝΟΥΣ', 'ΟΥΣΤΑΤΗ', 'ΟΥΣΤΑΤΑ', 'ΕΣΤΕΡΟΝ', 'ΟΥΣΤΑΤΟ', 'ΩΤΕΡΟΥΣ',
                       'ΩΤΑΤΟΥΣ', 'ΥΤΕΡΕΣ', 'ΩΜΕΝΟΥ', 'ΟΤΑΤΩΝ', 'ΕΣΤΑΤΟ', 'ΕΣΤΑΤΗ', 'ΥΤΑΤΩΝ', 'ΥΤΕΡΗΣ', 'ΟΜΕΝΟΣ',
                       'ΟΤΕΡΟΙ', 'ΟΤΕΡΩΝ', 'ΥΤΑΤΟΣ', 'ΥΤΑΤΟΥ', 'ΕΣΤΑΤΑ', 'ΥΤΑΤΗΣ', 'ΟΤΕΡΟΣ', 'ΟΤΕΡΟΥ', 'ΥΤΑΤΕΣ',
                       'ΟΤΕΡΕΣ', 'ΥΤΕΡΟΙ', 'ΥΤΕΡΩΝ', 'ΑΙΤΕΡΟ', 'ΟΤΕΡΗΣ', 'ΥΤΕΡΟΣ', 'ΑΙΤΕΡΗ', 'ΑΙΤΕΡΑ', 'ΜΕΝΟΥΣ',
                       'ΥΤΕΡΟΥ', 'ΩΜΕΝΗΣ', 'ΩΜΕΝΩΝ', 'ΩΜΕΝΕΣ', 'ΟΥΜΕΝΟ', 'ΟΥΜΕΝΗ', 'ΟΥΜΕΝΑ', 'ΟΜΕΝΕΣ', 'ΩΜΕΝΟΣ',
                       'ΟΜΕΝΗΣ', 'ΟΜΕΝΩΝ', 'ΕΣΤΕΡΟ', 'ΕΣΤΕΡΗ', 'ΕΣΤΕΡΑ', 'ΟΤΑΤΟΣ', 'ΟΤΑΤΗΣ', 'ΟΜΕΝΟΥ', 'ΟΤΑΤΟΙ',
                       'ΥΤΑΤΟΙ', 'ΟΤΑΤΟΥ', 'ΗΜΕΝΗΣ', 'ΟΜΕΝΟΙ', 'ΗΜΕΝΟΥ', 'ΗΜΕΝΟΙ', 'ΗΜΕΝΩΝ', 'ΜΕΝΟΥΣ', 'ΗΜΕΝΟΣ',
                       'ΩΜΕΝΟΙ', 'ΟΤΑΤΕΣ', 'ΩΤΕΡΟΣ', 'ΩΤΕΡΟΥ', 'ΩΤΕΡΟΝ', 'ΩΤΕΡΟΙ', 'ΩΤΕΡΩΝ', 'ΩΤΕΡΗΣ', 'ΩΤΕΡΕΣ',
                       'ΩΤΕΡΑΣ', 'ΩΤΑΤΟΣ', 'ΩΤΑΤΟΥ', 'ΩΤΑΤΟΙ', 'ΩΤΑΤΩΝ', 'ΩΤΑΤΗΣ', 'ΩΤΑΤΕΣ', 'ΜΕΝΟΥ', 'ΜΕΝΗΣ',
                       'ΜΕΝΟΙ', 'ΜΕΝΩΝ', 'ΩΜΕΝΟ', 'ΩΜΕΝΗ', 'ΩΜΕΝΑ', 'ΥΤΕΡΑ', 'ΥΤΑΤΑ', 'ΥΤΕΡΟ', 'ΟΤΑΤΗ',  'ΜΕΝΕΣ',
                       'ΟΜΕΝΑ', 'ΩΜΕΝΟ', 'ΩΜΕΝΗ', 'ΟΤΕΡΟ', 'ΟΤΕΡΗ', 'ΕΙΣΕΣ', 'ΟΜΕΝΟ', 'ΟΜΕΝΗ', 'ΥΤΕΡΗ', 'ΟΤΕΡΑ',
                       'ΜΕΝΟΙ', 'ΥΤΑΤΗ', 'ΟΤΑΤΟ', 'ΟΤΑΤΑ', 'ΜΕΝΟΥ', 'ΜΕΝΟΣ', 'ΗΜΕΝΗ', 'ΜΕΝΩΝ', 'ΜΕΝΗΣ', 'ΗΜΕΝΟ',
                       'ΗΜΕΝΑ', 'ΟΝΤΑΣ', 'ΩΝΤΑΣ', 'ΩΤΕΡΟ', 'ΩΤΕΡΕ', 'ΩΤΕΡΗ', 'ΩΤΕΡΑ', 'ΩΤΑΤΟ', 'ΩΤΑΤΕ', 'ΩΤΑΤΗ',
                       'ΩΤΑΤΑ', 'ΜΕΝΟ', 'ΜΕΝΗ', 'ΜΕΝΑ', 'ΕΙΕΣ', 'ΕΙΩΝ', 'ΟΥΣ', 'ΕΩΣ', 'ΕΟΣ', 'ΩΣΑ', 'ΟΥΝ', 'ΕΙΣ', 'ΟΥΣ',
                       'ΕΩΝ', 'ΙΣ', 'ΟΣ', 'ΥΣ', 'ΟΥ', 'ΑΣ', 'ΗΣ', 'ΟΣ', 'ΕΣ', 'ΕΑ', 'ΩΝ', 'ΤΙ', 'ΕΙ', 'ΟΝ', 'ΑΝ', 'ΕΝ',
                       'ΙΝ', 'ΟΙ', 'Η', 'Α', 'Ο',  'Ι', 'Υ', 'Ε'],
        
        'singular_noun': ['ΟΥΣ', 'ΕΩΣ', 'ΕΟΣ', 'ΟΥΝ', 'ΕΙΣ', 'ΥΣ', 'ΩΣ', 'ΟΥ', 'ΑΣ', 'ΗΣ', 'ΟΣ', 'ΕΣ', 'ΩΝ', 'ΕΙ', 'ΟΝ',
                          'ΑΝ', 'ΕΝ', 'ΙΝ', 'ΟΙ', 'ΙΣ', 'Η', 'Α', 'Ω', 'Ο', 'Ι', 'Ε'],
        
        'plural_noun': ['ΕΙΣΕΣ', 'ΕΙΣΩΝ', 'ΙΑΔΕΣ', 'ΙΑΔΩΝ', 'ΟΥΔΕΣ', 'ΟΥΔΩΝ', 'ΙΜΑΤΑ', 'ΟΥΣ', 'ΕΙΣ', 'ΕΩΝ', 'ΟΙ', 'ΩΝ',
                        'ΕΣ', 'ΕΑ', 'Α', 'Η'],
        
        'adverb': ['ΟΥΣΤΑΤΑ', 'ΑΙΤΕΡΑ', 'ΑΙΤΕΡΩΣ', 'ΟΤΑΤΑ', 'ΕΣΤΑΤΑ', 'ΥΤΑΤΑ', 'ΟΤΕΡΟ', 'ΟΤΕΡΑ', 'ΕΣΤΕΡΑ', 'ΥΤΕΡΑ',
                   'ΑΣΙΑ', 'ΜΕΝΑ', 'ΕΩΣ', 'ΤΑΤΑ', 'ΩΣ', 'ΟΥ', 'Α', 'Υ', 'Ο'],
        
        'irregular_adjective': ['ΤΕΡΟΥΣ', 'ΤΕΡΟΣ', 'ΤΕΡΟΝ', 'ΤΕΡΟΥ', 'ΤΕΡΗΣ', 'ΤΕΡΟΙ', 'ΤΕΡΩΝ', 'ΤΕΡΕΣ', 'ΤΑΤΟΣ',
                                'ΤΑΤΟΥ', 'ΤΑΤΗΣ', 'ΤΑΤΟΙ', 'ΤΑΤΩΝ', 'ΤΑΤΕΣ', 'ΤΕΡΟ', 'ΤΕΡΗ', 'ΤΕΡΑ', 'ΤΑΤΟ', 'ΤΑΤΗ',
                                'ΤΑΤΑ']

    }
}