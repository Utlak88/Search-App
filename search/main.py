import json
import os
import itertools


class ImportJSON:
    """
    Importing JSON user, organization, and tickets data.
    """

    def __init__(self):
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'organizations.json')) as org_json_file:
            self.organizations = json.load(org_json_file)
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'tickets.json')) as tickets_json_file:
            self.tickets = json.load(tickets_json_file)
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'users.json')) as users_json_file:
            self.users = json.load(users_json_file)


class SearchUsers(ImportJSON):
    """
    Processes User JSON data and returns the following:

    - User search results for a seach term / value pair
    - All available user search terms
    - All user search values for a search term
    - All user tags
    - User search entries that contain a specified tag
    - Search terms missing from user entries
    """

    def __init__(self, key=None, value=None):
        """
        Processes User JSON data and returns the following:

        - User search results for a seach term / value pair
        - All available user search terms
        - All user search values for a search term
        - All user tags
        - User search entries that contain a specified tag
        - Search terms missing from user entries
    
        :param key: Search term
        :param value: Search value
        """

        def catch(func, handle=lambda e: 'none', *args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                return handle(e)

        super().__init__()

        if key is not None:
            self.key = str(key)
        if value is not None:
            self.value = value
        if key and value is not None:
            self.index = [catch(lambda: i) for i in range(len(self.users))
                          if self.value == catch(lambda: self.users[i][self.key])
                          and catch(lambda: self.users[i][self.key]) != 'none']

    def all_search_fields(self):
        """
        Do not enter a search term or value when using this method.

        :return:  All available user search terms.
        """

        return set([list(itertools.chain.from_iterable(list(self.users[i].keys()) for i in range(len(self.users))))][0])

    def all_values_for_key(self):
        """
        Enter a user search term and do not enter a search value when using this method.

        :return: All user search values for a search term.
        """

        def catch(func, handle=lambda e: 'none', *args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                return handle(e)

        return [catch(lambda: i[self.key]) for i in self.users if catch(lambda: i[self.key]) != 'none']

    def check_missing_values(self):
        """
        Do not enter a search term or value when using this method.

        :return: Search terms missing from user entries.
        """

        all_keys = list(self.all_search_fields())

        missing_values = [(int_iter, [i for i in all_keys if i not in list(self.users[int_iter].keys())])
                          for int_iter in range(len(self.users))]

        missing_values_statement = ['User with \'_id\' ' + str(self.users[j]['_id']) + ' is missing ' +
                                    str(sorted([i for i in missing_values[j][1]])).replace('[', '').replace(']', '')
                                    + '.' for j in range(len(self.users)) if len(missing_values[j][1]) != 0]

        if len(missing_values_statement) == 0:
            return 'No user entries are empty.'
        else:
            return missing_values_statement

    def searchresults(self):
        """
        Enter a search term and value when using this method.

        :return: User search results for a seach term / value pair.
        """

        try:
            return [self.users[i] for i in self.index]
        except AttributeError:
            pass

    def alltags(self):
        """
        Do not enter a search term or value when using this method.

        :return: All user tags.
        """

        return set(list(itertools.chain.from_iterable([i['tags'] for i in self.users])))

    def usersbytag(self):
        """
        Enter a user tag as the search value and do not enter a search term when using this method.

        :return: User search entries that contain specified tag.
        """

        try:
            tag_index = [i for i, j in enumerate(self.users) if self.value in j['tags']]
            return [self.users[i] for i in tag_index]
        except AttributeError:
            pass


class SearchOrganizations(ImportJSON):
    """
    Processes Organization JSON data and returns the following:

    - Organization search results for a seach term / value pair
    - All available organization search terms
    - All organization search values for a search term
    - All organization tags
    - Organization search entries that contain a specified tag
    - Search terms missing from user entries
    """

    def __init__(self, key=None, value=None):
        """
        Processes Organization JSON data and returns the following:

        - Organization search results for a seach term / value pair
        - All available organization search terms
        - All organization search values for a search term
        - All organization tags
        - All organization domain names
        - Organization search entries that contain a specified tag
        - Search terms missing from organization entries

        :param key: Search term
        :param value: Search value
        """

        def catch(func, handle=lambda e: 'none', *args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                return handle(e)

        super().__init__()

        if key is not None:
            self.key = str(key)
        if value is not None:
            self.value = value
        if key and value is not None:
            self.index = [catch(lambda: i) for i in range(len(self.organizations))
                          if self.value == catch(lambda: self.organizations[i][self.key])
                          and catch(lambda: self.organizations[i][self.key]) != 'none']

    def all_search_fields(self):
        """
        Do not enter a search term or value when using this method.

        :return: All available organization search terms.
        """

        return set([list(
            itertools.chain.from_iterable(list(self.organizations[i].keys())
                                          for i in range(len(self.organizations))))][0])

    def all_values_for_key(self):
        """
        Enter an organization search term and do not enter a search value when using this method.

        :return: All organization search values for a search term.
        """

        def catch(func, handle=lambda e: 'none', *args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                return handle(e)

        return [catch(lambda: i[self.key]) for i in self.organizations if catch(lambda: i[self.key]) != 'none']

    def check_missing_values(self):
        """
        Do not enter a search term or value when using this method.

        :return: Search terms missing from organization entries.
        """

        all_keys = list(self.all_search_fields())

        missing_values = [(int_iter, [i for i in all_keys if i not in list(self.organizations[int_iter].keys())])
                          for int_iter in range(len(self.organizations))]

        missing_values_statement = ['Organization with \'_id\' ' + str(self.organizations[j]['_id']) + ' is missing ' +
                                    str(sorted([i for i in missing_values[j][1]])).replace('[', '').replace(']', '')
                                    + '.' for j in range(len(self.organizations)) if len(missing_values[j][1]) != 0]

        if len(missing_values_statement) == 0:
            return 'No organization entries are empty.'
        else:
            return missing_values_statement

    def searchresults(self):
        """
        Enter a search term and value when using this method.

        :return: Organization search results for a seach term / value pair.
        """

        try:
            return [self.organizations[i] for i in self.index]
        except AttributeError:
            pass

    def alltags(self):
        """
        Do not enter a search term or value when using this method.

        :return: All organization tags.
        """

        return set(list(itertools.chain.from_iterable([i['tags'] for i in self.organizations])))

    def alldomains(self):
        """
        Do not enter a search term or value when using this method.

        :return: All organization domain names
        """

        return set(list(itertools.chain.from_iterable([i['domain_names'] for i in self.organizations])))

    def organizationsbytag(self):
        """
        Enter an organization tag as the search value and do not enter a search term when using this method.

        :return: Organization search entries that contain specified tag.
        """

        try:
            tag_index = [i for i, j in enumerate(self.organizations) if self.value in j['tags']]
            return [self.organizations[i] for i in tag_index]
        except AttributeError:
            pass

    def organizationsbydomain(self):
        """
        Enter an organization domain name as the search value and do not enter a search term when using this method.

        :return: Organization search entries that contain specified tag.
        """

        try:
            domain_index = [i for i, j in enumerate(self.organizations) if self.value in j['domain_names']]
            return [self.organizations[i] for i in domain_index]
        except AttributeError:
            pass


class SearchTickets(ImportJSON):
    """
    Processes Ticket JSON data and returns the following:

    - Ticket search results for a seach term / value pair
    - All available ticket search terms
    - All ticket search values for a search term
    - All ticket tags
    - Ticket search entries that contain a specified tag
    - Search terms missing from ticket entries
    """

    def __init__(self, key=None, value=None):
        """
        Processes Ticket JSON data and returns the following:

        - Ticket search results for a seach term / value pair
        - All available ticket search terms
        - All ticket search values for a search term
        - All ticket tags
        - Ticket search entries that contain a specified tag
        - Search terms missing from ticket entries

        :param key: Search term
        :param value: Search value
        """

        def catch(func, handle=lambda e: 'none', *args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                return handle(e)

        super().__init__()

        if key is not None:
            self.key = str(key)
        if value is not None:
            self.value = value
        if key and value is not None:
            self.index = [catch(lambda: i) for i in range(len(self.tickets))
                          if self.value == catch(lambda: self.tickets[i][self.key])
                          and catch(lambda: self.tickets[i][self.key]) != 'none']

    def all_search_fields(self):
        """
        Do not enter a search term or value when using this method.

        :return: All available ticket search terms.
        """

        return set(
            [list(itertools.chain.from_iterable(list(self.tickets[i].keys()) for i in range(len(self.tickets))))][0])

    def all_values_for_key(self):
        """
        Enter a ticket search term and do not enter a search value when using this method.

        :return: All ticket search values for a search term.
        """

        def catch(func, handle=lambda e: 'none', *args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                return handle(e)

        return [catch(lambda: i[self.key]) for i in self.tickets if catch(lambda: i[self.key]) != 'none']

    def check_missing_values(self):
        """
        Do not enter a search term or value when using this method.

        :return: Search terms missing from ticket entries.
        """

        all_keys = list(self.all_search_fields())

        missing_values = [(int_iter, [i for i in all_keys if i not in list(self.tickets[int_iter].keys())])
                          for int_iter in range(len(self.tickets))]

        missing_values_statement = ['Ticket with \'_id\' ' + str(self.tickets[j]['_id']) + ' is missing '
                                    + str(sorted([i for i in missing_values[j][1]])).replace('[', '').replace(']', '')
                                    + '.' for j in range(len(self.tickets)) if len(missing_values[j][1]) != 0]

        if len(missing_values_statement) == 0:
            return 'No ticket entries are empty.'
        else:
            return missing_values_statement

    def searchresults(self):
        """
        Enter a search term and value when using this method.

        :return: Ticket search results for a seach term / value pair.
        """

        try:
            return [self.tickets[i] for i in self.index]
        except AttributeError:
            pass

    def alltags(self):
        """
        Do not enter a search term or value when using this method.

        :return: All ticket tags.
        """

        return set(list(itertools.chain.from_iterable([i['tags'] for i in self.tickets])))

    def ticketsbytag(self):
        """
        Enter a ticket tag as the search value and do not enter a search term when using this method.

        :return: Ticket search entries that contain specified tag.
        """

        try:
            tag_index = [i for i, j in enumerate(self.tickets) if self.value in j['tags']]
            return [self.tickets[i] for i in tag_index]
        except AttributeError:
            pass
