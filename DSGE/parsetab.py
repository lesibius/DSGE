
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEleftEXPrightUMINUSCOMMA DIVIDE EQUALS EXP FLOAT INTEGER LPAREN MINUS NAME PLUS RPAREN TIMESstatement : NAME EQUALS atom\n        arglist : arglist COMMA NAME\n                   | arglist COMMA number\n                   | number\n                   | NAME\n        parameters : LPAREN RPAREN \n                      | LPAREN arglist RPARENfunction : NAME parametersnumber : INTEGER \n                      | FLOAT\n        number : number PLUS number\n               | number MINUS number\n               | number TIMES number\n               | number DIVIDE number\n               | number EXP number\n        \n        atom : atom PLUS atom\n             | atom MINUS atom\n             | atom TIMES atom\n             | atom DIVIDE atom\n             | atom EXP atom\n        atom : number PLUS atom\n                | number MINUS atom\n                | number TIMES atom\n                | number DIVIDE atom\n                | number EXP atomnumber : MINUS number %prec UMINUSnumber : LPAREN number RPARENatom : LPAREN atom RPARENvariable : NAMEatom : numberatom : variableatom : function'
    
_lr_action_items = {'NAME':([0,3,8,14,15,16,17,18,19,22,23,24,25,26,57,],[2,4,4,31,4,4,4,4,4,4,4,4,4,4,63,]),'$end':([1,4,5,7,9,10,11,12,13,20,29,33,34,35,36,37,44,45,46,47,48,49,50,51,52,53,54,55,56,58,59,60,61,62,],[0,-29,-1,-30,-31,-32,-9,-10,-8,-26,-6,-16,-17,-18,-19,-20,-11,-21,-12,-22,-13,-23,-14,-24,-15,-25,-28,-27,-7,-12,-11,-13,-14,-15,]),'EQUALS':([2,],[3,]),'LPAREN':([3,4,6,8,14,15,16,17,18,19,21,22,23,24,25,26,38,39,40,41,42,57,],[8,14,21,8,21,8,8,8,8,8,21,8,8,8,8,8,21,21,21,21,21,21,]),'INTEGER':([3,6,8,14,15,16,17,18,19,21,22,23,24,25,26,38,39,40,41,42,57,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'FLOAT':([3,6,8,14,15,16,17,18,19,21,22,23,24,25,26,38,39,40,41,42,57,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'MINUS':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,],[6,-29,16,6,23,6,-31,-32,-9,-10,-8,6,6,6,6,6,6,-26,6,6,6,6,6,6,16,23,-6,38,-16,-17,-18,-19,-20,6,6,6,6,6,38,-11,-21,-12,-22,-13,-23,-14,-24,-15,-25,-28,-27,-7,6,-12,-11,-13,-14,-15,38,]),'PLUS':([4,5,7,9,10,11,12,13,20,27,28,29,32,33,34,35,36,37,43,44,45,46,47,48,49,50,51,52,53,54,55,56,58,59,60,61,62,64,],[-29,15,22,-31,-32,-9,-10,-8,-26,15,22,-6,39,-16,-17,-18,-19,-20,39,-11,-21,-12,-22,-13,-23,-14,-24,-15,-25,-28,-27,-7,-12,-11,-13,-14,-15,39,]),'TIMES':([4,5,7,9,10,11,12,13,20,27,28,29,32,33,34,35,36,37,43,44,45,46,47,48,49,50,51,52,53,54,55,56,58,59,60,61,62,64,],[-29,17,24,-31,-32,-9,-10,-8,-26,17,24,-6,40,17,17,-18,-19,-20,40,24,17,24,17,-13,-23,-14,-24,-15,-25,-28,-27,-7,40,40,-13,-14,-15,40,]),'DIVIDE':([4,5,7,9,10,11,12,13,20,27,28,29,32,33,34,35,36,37,43,44,45,46,47,48,49,50,51,52,53,54,55,56,58,59,60,61,62,64,],[-29,18,25,-31,-32,-9,-10,-8,-26,18,25,-6,41,18,18,-18,-19,-20,41,25,18,25,18,-13,-23,-14,-24,-15,-25,-28,-27,-7,41,41,-13,-14,-15,41,]),'EXP':([4,5,7,9,10,11,12,13,20,27,28,29,32,33,34,35,36,37,43,44,45,46,47,48,49,50,51,52,53,54,55,56,58,59,60,61,62,64,],[-29,19,26,-31,-32,-9,-10,-8,-26,19,26,-6,42,19,19,19,19,-20,42,26,19,26,19,26,19,26,19,-15,-25,-28,-27,-7,42,42,42,42,-15,42,]),'RPAREN':([4,7,9,10,11,12,13,14,20,27,28,29,30,31,32,33,34,35,36,37,43,44,45,46,47,48,49,50,51,52,53,54,55,56,58,59,60,61,62,63,64,],[-29,-30,-31,-32,-9,-10,-8,29,-26,54,55,-6,56,-5,-4,-16,-17,-18,-19,-20,55,-11,-21,-12,-22,-13,-23,-14,-24,-15,-25,-28,-27,-7,-12,-11,-13,-14,-15,-2,-3,]),'COMMA':([11,12,20,30,31,32,55,58,59,60,61,62,63,64,],[-9,-10,-26,57,-5,-4,-27,-12,-11,-13,-14,-15,-2,-3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'atom':([3,8,15,16,17,18,19,22,23,24,25,26,],[5,27,33,34,35,36,37,45,47,49,51,53,]),'number':([3,6,8,14,15,16,17,18,19,21,22,23,24,25,26,38,39,40,41,42,57,],[7,20,28,32,7,7,7,7,7,43,44,46,48,50,52,58,59,60,61,62,64,]),'variable':([3,8,15,16,17,18,19,22,23,24,25,26,],[9,9,9,9,9,9,9,9,9,9,9,9,]),'function':([3,8,15,16,17,18,19,22,23,24,25,26,],[10,10,10,10,10,10,10,10,10,10,10,10,]),'parameters':([4,],[13,]),'arglist':([14,],[30,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> NAME EQUALS atom','statement',3,'p_statement','Equation_parser.py',100),
  ('arglist -> arglist COMMA NAME','arglist',3,'p_arglist','Equation_parser.py',113),
  ('arglist -> arglist COMMA number','arglist',3,'p_arglist','Equation_parser.py',114),
  ('arglist -> number','arglist',1,'p_arglist','Equation_parser.py',115),
  ('arglist -> NAME','arglist',1,'p_arglist','Equation_parser.py',116),
  ('parameters -> LPAREN RPAREN','parameters',2,'p_parameters','Equation_parser.py',126),
  ('parameters -> LPAREN arglist RPAREN','parameters',3,'p_parameters','Equation_parser.py',127),
  ('function -> NAME parameters','function',2,'p_function','Equation_parser.py',134),
  ('number -> INTEGER','number',1,'p_number','Equation_parser.py',139),
  ('number -> FLOAT','number',1,'p_number','Equation_parser.py',140),
  ('number -> number PLUS number','number',3,'p_number_binop','Equation_parser.py',145),
  ('number -> number MINUS number','number',3,'p_number_binop','Equation_parser.py',146),
  ('number -> number TIMES number','number',3,'p_number_binop','Equation_parser.py',147),
  ('number -> number DIVIDE number','number',3,'p_number_binop','Equation_parser.py',148),
  ('number -> number EXP number','number',3,'p_number_binop','Equation_parser.py',149),
  ('atom -> atom PLUS atom','atom',3,'p_atom_binop','Equation_parser.py',164),
  ('atom -> atom MINUS atom','atom',3,'p_atom_binop','Equation_parser.py',165),
  ('atom -> atom TIMES atom','atom',3,'p_atom_binop','Equation_parser.py',166),
  ('atom -> atom DIVIDE atom','atom',3,'p_atom_binop','Equation_parser.py',167),
  ('atom -> atom EXP atom','atom',3,'p_atom_binop','Equation_parser.py',168),
  ('atom -> number PLUS atom','atom',3,'p_atom_number_binop_atom','Equation_parser.py',174),
  ('atom -> number MINUS atom','atom',3,'p_atom_number_binop_atom','Equation_parser.py',175),
  ('atom -> number TIMES atom','atom',3,'p_atom_number_binop_atom','Equation_parser.py',176),
  ('atom -> number DIVIDE atom','atom',3,'p_atom_number_binop_atom','Equation_parser.py',177),
  ('atom -> number EXP atom','atom',3,'p_atom_number_binop_atom','Equation_parser.py',178),
  ('number -> MINUS number','number',2,'p_number_uminus','Equation_parser.py',184),
  ('number -> LPAREN number RPAREN','number',3,'p_number_group','Equation_parser.py',188),
  ('atom -> LPAREN atom RPAREN','atom',3,'p_atom_group','Equation_parser.py',192),
  ('variable -> NAME','variable',1,'p_variable','Equation_parser.py',196),
  ('atom -> number','atom',1,'p_atom_number','Equation_parser.py',200),
  ('atom -> variable','atom',1,'p_atom_variable','Equation_parser.py',204),
  ('atom -> function','atom',1,'p_atom_function','Equation_parser.py',208),
]
