import csv


class DataBus(object):
    def __init__(self, filename):
        """
        :param filename: *string*
        """
        self.filename = filename

    def write_header(self, sensors):
        """

        :param sensors: *list* with sensornames
        :return: *None*
        """
        with open(self.filename, mode='wb') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';')
            csv_writer.writerow(['timestamp'] + sensors)

    def write_content_row(self, content):
        """

        :param content: *list* with timestamp an sensorvalues
        :return: *None*
        """
        with open(self.filename, mode='ab') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';')
            csv_writer.writerow(content)
