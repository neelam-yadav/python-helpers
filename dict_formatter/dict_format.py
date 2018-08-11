from re import finditer
import ast


class DictFormat:
    def _get_placeholders(self, input):
        placeholders = {}
        try:
            for match in finditer(r"\{([0-9_]+)\}", input):
                placeholders[int(match.group().strip('{}'))] = match.group()
        except Exception:
            raise
        return placeholders

    def format(self, input, replace):
        '''
        Formats dictionary
        :param input (dict): dictionary
        :param replace (list): values to replace
        :return:
        '''
        input = str(input)
        output = input
        try:
            placeholders = self._get_placeholders(input)
            for k, v in placeholders.items():
                output = output.replace(v, replace[k])
            output = ast.literal_eval(output)
        except Exception as err:
            print(err)
        return output


dict_format = DictFormat()