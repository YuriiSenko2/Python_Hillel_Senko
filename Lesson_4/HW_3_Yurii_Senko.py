print('''In order to enjoy our app use the following key words:
add - to add notes;
earliest - to display the notes in a chronological order from old to new;
latest - to display the notes in a chronological order from new to old;
longest - to display the notes in length from longest to shortest;
shortest - to display the notes in length from shortest to longest
Exit - to exit the program''')

key_word = input('\nInput the key-word: ')
# Input the key-word from the list above

allowed_words = 'add', 'earliest', 'latest', 'longest', 'shortest'
# The only words along with 'Exit' the program will process

notes_list = []
# The list to supplement

while key_word != 'Exit':
    # The program will be closed by entering the 'Exit' as a key-word

    if key_word == 'add':
        """
        After entering 'add' as a key word
        User is asked to add a note(notes)
        Then this note supplements the notes_list(notes_list.append(notes)
        And then the user choose the next action by entering the key-word
        """
        notes = input('Input a note: ')
        notes_list.append(notes)
        key_word = input('Input the key-word: ')

    elif key_word == 'earliest':
        """
        After entering 'earliest' as a key word
        Then the user sees the notes in a chronological order from old to new (print(notes_list);
        And then the user choose the next action by entering the key-word
        """
        print(notes_list)
        key_word = input('Input the key-word: ')

    elif key_word == 'latest':
        """
        After entering 'latest' as a key word
        The list is sorted by chronological order from new to old (notes_list.reverse());
        Then the user sees the notes in a chronological order from new to old (print(notes_list);
        And then the user choose the next action by entering the key-word
        """
        notes_list.reverse()
        print(notes_list)
        key_word = input('Input the key-word: ')

    elif key_word == 'longest':
        """
        After entering 'longest' as a key word
        The list is sorted in length from longest to shortest (notes_list.sort(key=len, reverse=True));
        Then the user sees the notes in length from longest to shortest (print(notes_list);
        And then the user choose the next action by entering the key-word
        """
        notes_list.sort(key=len, reverse=True)
        print(notes_list)
        key_word = input('Input the key-word: ')

    elif key_word == 'shortest':
        """
        After entering 'shortest' as a key word
        The list is sorted in length from shortest to longest (notes_list.sort(key=len));
        Then the user sees the notes in length from shortest to longest (print(notes_list);
        And then the user choose the next action by entering the key-word
        """
        notes_list.sort(key=len)
        print(notes_list)
        key_word = input('Input the key-word: ')

    elif key_word not in allowed_words:
        """"
        If the user enters anything different from the values of 'allowed_words' variable or from 'Exit' key-word
        The error message is displayed (print('Wrong key-word.\nUse the key-words from the list\n'))
        And then the user choose the next action by entering the key-word
        """
        print('Wrong key-word.\nUse the key-words from the list\n')
        key_word = input('Input the key-word: ')

