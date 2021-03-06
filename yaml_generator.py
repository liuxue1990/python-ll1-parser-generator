from ll1_symbols import * 

YAML_OUTPUT = """terminals: %s
non-terminals: %s
eof-marker: %s
error-marker: %s
start-symbol: %s
productions: %s
table: %s"""

YAML_OUTPUT_NO_TABLE = """terminals: %s
non-terminals: %s
eof-marker: %s
error-marker: %s
start-symbol: %s
productions: %s"""

class YamlGenerator(object):
	"""docstring for yaml_generator"""
	def __init__(self, grammar):
		self.grammar = grammar

	def print_yaml(self, ll1_table = None):
		def convert_list_str(a_list):
			return "[%s]" % (", ".join(a_list))

		def convert_dict_str(a_dict):
			return "{%s}" % ", ".join(["%s: %s" % (key, value) 
				for key, value in a_dict.items()])

		def convert_dict_dict_str(a_dict):
			return "\n  %s" % ("\n  ".join(["%s: %s" % (key, convert_dict_str(value)) 
				for key, value in a_dict.items()]))

		def convert_dict_list_str(a_dict):
			return "{%s}" % (", \n ".join(["%s: %s" % (key, convert_list_str(value)) 
				for key, value in a_dict.items()]))

		def convert_dict_dict_list_str(a_dict):
			return "\n  %s" % ("\n  ".join(["%s: %s" % (key, convert_dict_list_str(value)) 
				for key, value in a_dict.items()]))
		if ll1_table:
			return YAML_OUTPUT % (convert_list_str(list(self.grammar.term)), 
									convert_list_str(list(self.grammar.non_term)), 
									EOF, 
									ERROR_MARKER, 
									self.grammar.goal, 
									convert_dict_dict_list_str(self.convert_production()), 
									convert_dict_dict_str(ll1_table))
		else:
			return YAML_OUTPUT_NO_TABLE % (convert_list_str(list(self.grammar.term)), 
									convert_list_str(list(self.grammar.non_term)), 
									EOF, 
									ERROR_MARKER, 
									self.grammar.goal, 
									convert_dict_dict_list_str(self.convert_production()))

	def convert_production(self):
				return {idx : {production.left_hand.lexeme : [item.lexeme for item in production.right_hand if item.lexeme is not EPSILON]} for idx, production in enumerate(self.grammar.production)}
