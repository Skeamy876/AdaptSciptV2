
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocGELEEQNEGTLTORleftADDSUBleftMULDIVrightUNARYACCEPT ADAPT ADD AND COMMENTS DIV ELSE EQ EQUAL FLOAT FLOAT_VALUE FOR FUNC GE GT IDENTIFIER IF INIT INT INT_VALUE LE LT MUL NE OR PRINT RETURN STRING STRING_VALUE SUB UNARY VOID WHILE WHITESPACEprogram : programStartprogramStart : FUNC INIT "(" ")" "{" statements "}" statements : statement\n                  | statements statementstatement : function_calls\n                | condition\n                | function_declarations\n                | expression\n                | loops\n                | RETURN variable\n                | ACCEPT "(" variable ")"\n                | PRINT "(" variable ")"\n                | ACCEPT "(" atoms ")"\n                | PRINT "(" STRING_VALUE atoms ")" ")"function_declarations : function_declarationfunction_declaration : FUNC IDENTIFIER "(" ")" ":" datatype "{" function_body "}" function_body : statementsfunction_calls : IDENTIFIER "(" ")"\n                     | IDENTIFIER "(" ")" function_calls\n                     | IDENTIFIER "(" parameters ")" \n                     | IDENTIFIER "(" parameters ")" function_callsvariable : IDENTIFIER parameters : parameterListparameterList : parameter\n                    | parameter "," parameterListparameter : datatype IDENTIFIERdatatype : INT\n                    | FLOAT\n                    | STRING\n                    | ADAPT\n                    | VOIDatoms : INT_VALUE\n                | FLOAT_VALUE\n                | STRING_VALUE\n                | variableparen_expr : "(" expression ")"binary_expr : variable ADD expression\n                    | variable SUB expression\n                    | variable MUL expression\n                    | variable DIV expression\n                    | variable OR expression\n                    | variable LE expression\n                    | variable GE expression\n                    | variable EQ expression\n                    | variable NE expression\n                    | variable GT expression\n                    | variable LT expression\n                    | UNARY expression\n                    | expression UNARYexpression : atoms\n                    | paren_expr\n                    | binary_exprcondition : IF expression "{" statements "}"\n                    | IF expression "{" statements "}" ELSE "{" statements "}"loops : loop\n                | loop loopsloop : forLoop\n                | whileLoopforLoop : FOR "(" expression ";" condition ";" expression ")" "{" statements "}"whileLoop : WHILE "(" condition ")" "{" statements "}"'
    
_lr_action_items = {'FUNC':([0,7,10,11,12,13,14,15,16,18,21,22,23,25,26,27,28,29,30,32,33,38,40,41,42,58,59,63,64,65,66,67,68,69,70,71,72,73,74,79,89,93,94,95,99,100,103,108,110,112,114,117,118,119,121,123,124,126,127,128,129,130,],[3,8,8,-3,-5,-6,-7,-8,-9,-35,-50,-34,-22,-15,-51,-52,-55,-32,-33,-57,-58,-22,-4,-49,-10,-56,-48,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-18,8,-11,-13,-12,-19,-20,8,-21,-53,8,-14,8,8,8,-60,8,8,-16,-54,8,8,-59,]),'$end':([1,2,39,],[0,-1,-2,]),'INIT':([3,],[4,]),'(':([4,7,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,58,59,60,63,64,65,66,67,68,69,70,71,72,73,74,79,89,93,94,95,98,99,100,103,108,110,112,114,116,117,118,119,121,123,124,126,127,128,129,130,],[5,9,9,9,-3,-5,-6,-7,-8,-9,-35,54,55,-50,-34,56,9,-15,-51,-52,-55,-32,-33,9,-57,-58,60,61,62,-22,-4,-49,-10,9,9,9,9,9,9,9,9,9,9,9,-56,-48,9,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-18,9,-11,-13,-12,56,-19,-20,9,-21,-53,9,-14,9,9,9,9,-60,9,9,-16,-54,9,9,-59,]),')':([5,18,21,22,26,27,29,30,37,38,41,56,59,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,81,82,91,96,97,102,107,109,110,120,127,],[6,-35,-50,-34,-51,-52,-32,-33,63,-22,-49,79,-48,92,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,93,94,95,100,-23,-24,105,107,-35,-26,114,-25,-53,125,-54,]),'{':([6,18,21,22,26,27,29,30,38,41,57,59,63,64,65,66,67,68,69,70,71,72,73,74,84,85,86,87,88,105,113,115,125,],[7,-35,-50,-34,-51,-52,-32,-33,-22,-49,89,-48,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-27,-28,-29,-30,-31,112,118,119,128,]),'RETURN':([7,10,11,12,13,14,15,16,18,21,22,23,25,26,27,28,29,30,32,33,38,40,41,42,58,59,63,64,65,66,67,68,69,70,71,72,73,74,79,89,93,94,95,99,100,103,108,110,112,114,117,118,119,121,123,124,126,127,128,129,130,],[17,17,-3,-5,-6,-7,-8,-9,-35,-50,-34,-22,-15,-51,-52,-55,-32,-33,-57,-58,-22,-4,-49,-10,-56,-48,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-18,17,-11,-13,-12,-19,-20,17,-21,-53,17,-14,17,17,17,-60,17,17,-16,-54,17,17,-59,]),'ACCEPT':([7,10,11,12,13,14,15,16,18,21,22,23,25,26,27,28,29,30,32,33,38,40,41,42,58,59,63,64,65,66,67,68,69,70,71,72,73,74,79,89,93,94,95,99,100,103,108,110,112,114,117,118,119,121,123,124,126,127,128,129,130,],[19,19,-3,-5,-6,-7,-8,-9,-35,-50,-34,-22,-15,-51,-52,-55,-32,-33,-57,-58,-22,-4,-49,-10,-56,-48,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-18,19,-11,-13,-12,-19,-20,19,-21,-53,19,-14,19,19,19,-60,19,19,-16,-54,19,19,-59,]),'PRINT':([7,10,11,12,13,14,15,16,18,21,22,23,25,26,27,28,29,30,32,33,38,40,41,42,58,59,63,64,65,66,67,68,69,70,71,72,73,74,79,89,93,94,95,99,100,103,108,110,112,114,117,118,119,121,123,124,126,127,128,129,130,],[20,20,-3,-5,-6,-7,-8,-9,-35,-50,-34,-22,-15,-51,-52,-55,-32,-33,-57,-58,-22,-4,-49,-10,-56,-48,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-18,20,-11,-13,-12,-19,-20,20,-21,-53,20,-14,20,20,20,-60,20,20,-16,-54,20,20,-59,]),'IDENTIFIER':([7,8,9,10,11,12,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,58,59,60,63,64,65,66,67,68,69,70,71,72,73,74,78,79,83,84,85,86,87,88,89,93,94,95,99,100,103,108,110,112,114,116,117,118,119,121,123,124,126,127,128,129,130,],[23,36,38,23,-3,-5,-6,-7,-8,-9,38,-35,-50,-34,-22,38,-15,-51,-52,-55,-32,-33,38,-57,-58,-22,-4,-49,-10,38,38,38,38,38,38,38,38,38,38,38,38,38,-56,-48,38,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,38,98,102,-27,-28,-29,-30,-31,23,-11,-13,-12,-19,98,23,-21,-53,23,-14,38,23,23,23,-60,23,23,-16,-54,23,23,-59,]),'IF':([7,10,11,12,13,14,15,16,18,21,22,23,25,26,27,28,29,30,32,33,38,40,41,42,58,59,61,63,64,65,66,67,68,69,70,71,72,73,74,79,89,93,94,95,99,100,103,104,108,110,112,114,117,118,119,121,123,124,126,127,128,129,130,],[24,24,-3,-5,-6,-7,-8,-9,-35,-50,-34,-22,-15,-51,-52,-55,-32,-33,-57,-58,-22,-4,-49,-10,-56,-48,24,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-18,24,-11,-13,-12,-19,-20,24,24,-21,-53,24,-14,24,24,24,-60,24,24,-16,-54,24,24,-59,]),'INT_VALUE':([7,9,10,11,12,13,14,15,16,18,21,22,23,24,25,26,27,28,29,30,31,32,33,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,58,59,60,63,64,65,66,67,68,69,70,71,72,73,74,78,79,89,93,94,95,99,100,103,108,110,112,114,116,117,118,119,121,123,124,126,127,128,129,130,],[29,29,29,-3,-5,-6,-7,-8,-9,-35,-50,-34,-22,29,-15,-51,-52,-55,-32,-33,29,-57,-58,-22,-4,-49,-10,29,29,29,29,29,29,29,29,29,29,29,29,-56,-48,29,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,29,-18,29,-11,-13,-12,-19,-20,29,-21,-53,29,-14,29,29,29,29,-60,29,29,-16,-54,29,29,-59,]),'FLOAT_VALUE':([7,9,10,11,12,13,14,15,16,18,21,22,23,24,25,26,27,28,29,30,31,32,33,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,58,59,60,63,64,65,66,67,68,69,70,71,72,73,74,78,79,89,93,94,95,99,100,103,108,110,112,114,116,117,118,119,121,123,124,126,127,128,129,130,],[30,30,30,-3,-5,-6,-7,-8,-9,-35,-50,-34,-22,30,-15,-51,-52,-55,-32,-33,30,-57,-58,-22,-4,-49,-10,30,30,30,30,30,30,30,30,30,30,30,30,-56,-48,30,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,30,-18,30,-11,-13,-12,-19,-20,30,-21,-53,30,-14,30,30,30,30,-60,30,30,-16,-54,30,30,-59,]),'STRING_VALUE':([7,9,10,11,12,13,14,15,16,18,21,22,23,24,25,26,27,28,29,30,31,32,33,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,58,59,60,63,64,65,66,67,68,69,70,71,72,73,74,78,79,89,93,94,95,99,100,103,108,110,112,114,116,117,118,119,121,123,124,126,127,128,129,130,],[22,22,22,-3,-5,-6,-7,-8,-9,-35,-50,-34,-22,22,-15,-51,-52,-55,-32,-33,22,-57,-58,-22,-4,-49,-10,22,22,22,22,22,22,22,22,22,22,22,22,78,-56,-48,22,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,22,-18,22,-11,-13,-12,-19,-20,22,-21,-53,22,-14,22,22,22,22,-60,22,22,-16,-54,22,22,-59,]),'UNARY':([7,9,10,11,12,13,14,15,16,18,21,22,23,24,25,26,27,28,29,30,31,32,33,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,57,58,59,60,63,64,65,66,67,68,69,70,71,72,73,74,79,89,90,93,94,95,99,100,103,108,110,112,114,116,117,118,119,120,121,123,124,126,127,128,129,130,],[31,31,31,-3,-5,-6,-7,41,-9,-35,-50,-34,-22,31,-15,-51,-52,-55,-32,-33,31,-57,-58,41,-22,-4,-49,-10,31,31,31,31,31,31,31,31,31,31,31,41,-56,41,31,-36,41,41,41,41,41,41,41,41,41,41,41,-18,31,41,-11,-13,-12,-19,-20,31,-21,-53,31,-14,31,31,31,31,41,-60,31,31,-16,-54,31,31,-59,]),'FOR':([7,10,11,12,13,14,15,16,18,21,22,23,25,26,27,28,29,30,32,33,38,40,41,42,58,59,63,64,65,66,67,68,69,70,71,72,73,74,79,89,93,94,95,99,100,103,108,110,112,114,117,118,119,121,123,124,126,127,128,129,130,],[34,34,-3,-5,-6,-7,-8,-9,-35,-50,-34,-22,-15,-51,-52,34,-32,-33,-57,-58,-22,-4,-49,-10,-56,-48,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-18,34,-11,-13,-12,-19,-20,34,-21,-53,34,-14,34,34,34,-60,34,34,-16,-54,34,34,-59,]),'WHILE':([7,10,11,12,13,14,15,16,18,21,22,23,25,26,27,28,29,30,32,33,38,40,41,42,58,59,63,64,65,66,67,68,69,70,71,72,73,74,79,89,93,94,95,99,100,103,108,110,112,114,117,118,119,121,123,124,126,127,128,129,130,],[35,35,-3,-5,-6,-7,-8,-9,-35,-50,-34,-22,-15,-51,-52,35,-32,-33,-57,-58,-22,-4,-49,-10,-56,-48,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-18,35,-11,-13,-12,-19,-20,35,-21,-53,35,-14,35,35,35,-60,35,35,-16,-54,35,35,-59,]),'}':([10,11,12,13,14,15,16,18,21,22,23,25,26,27,28,29,30,32,33,38,40,41,42,58,59,63,64,65,66,67,68,69,70,71,72,73,74,79,93,94,95,99,100,103,108,110,114,117,121,122,123,124,126,127,129,130,],[39,-3,-5,-6,-7,-8,-9,-35,-50,-34,-22,-15,-51,-52,-55,-32,-33,-57,-58,-22,-4,-49,-10,-56,-48,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-18,-11,-13,-12,-19,-20,110,-21,-53,-14,121,-60,126,-17,127,-16,-54,130,-59,]),';':([18,21,22,26,27,29,30,38,41,59,63,64,65,66,67,68,69,70,71,72,73,74,90,110,111,127,],[-35,-50,-34,-51,-52,-32,-33,-22,-49,-48,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,104,-53,116,-54,]),'ADD':([18,23,38,],[43,-22,-22,]),'SUB':([18,23,38,],[44,-22,-22,]),'MUL':([18,23,38,],[45,-22,-22,]),'DIV':([18,23,38,],[46,-22,-22,]),'OR':([18,23,38,],[47,-22,-22,]),'LE':([18,23,38,],[48,-22,-22,]),'GE':([18,23,38,],[49,-22,-22,]),'EQ':([18,23,38,],[50,-22,-22,]),'NE':([18,23,38,],[51,-22,-22,]),'GT':([18,23,38,],[52,-22,-22,]),'LT':([18,23,38,],[53,-22,-22,]),'INT':([56,101,106,],[84,84,84,]),'FLOAT':([56,101,106,],[85,85,85,]),'STRING':([56,101,106,],[86,86,86,]),'ADAPT':([56,101,106,],[87,87,87,]),'VOID':([56,101,106,],[88,88,88,]),',':([82,102,],[101,-26,]),':':([92,],[106,]),'ELSE':([110,],[115,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'programStart':([0,],[2,]),'statements':([7,89,112,118,119,128,],[10,103,117,123,124,129,]),'statement':([7,10,89,103,112,117,118,119,123,124,128,129,],[11,40,11,40,11,40,11,11,40,40,11,40,]),'function_calls':([7,10,79,89,100,103,112,117,118,119,123,124,128,129,],[12,12,99,12,108,12,12,12,12,12,12,12,12,12,]),'condition':([7,10,61,89,103,104,112,117,118,119,123,124,128,129,],[13,13,91,13,13,111,13,13,13,13,13,13,13,13,]),'function_declarations':([7,10,89,103,112,117,118,119,123,124,128,129,],[14,14,14,14,14,14,14,14,14,14,14,14,]),'expression':([7,9,10,24,31,43,44,45,46,47,48,49,50,51,52,53,60,89,103,112,116,117,118,119,123,124,128,129,],[15,37,15,57,59,64,65,66,67,68,69,70,71,72,73,74,90,15,15,15,120,15,15,15,15,15,15,15,]),'loops':([7,10,28,89,103,112,117,118,119,123,124,128,129,],[16,16,58,16,16,16,16,16,16,16,16,16,16,]),'variable':([7,9,10,17,24,31,43,44,45,46,47,48,49,50,51,52,53,54,55,60,78,89,103,112,116,117,118,119,123,124,128,129,],[18,18,18,42,18,18,18,18,18,18,18,18,18,18,18,18,18,75,77,18,97,18,18,18,18,18,18,18,18,18,18,18,]),'atoms':([7,9,10,24,31,43,44,45,46,47,48,49,50,51,52,53,54,60,78,89,103,112,116,117,118,119,123,124,128,129,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,76,21,96,21,21,21,21,21,21,21,21,21,21,21,]),'function_declaration':([7,10,89,103,112,117,118,119,123,124,128,129,],[25,25,25,25,25,25,25,25,25,25,25,25,]),'paren_expr':([7,9,10,24,31,43,44,45,46,47,48,49,50,51,52,53,60,89,103,112,116,117,118,119,123,124,128,129,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'binary_expr':([7,9,10,24,31,43,44,45,46,47,48,49,50,51,52,53,60,89,103,112,116,117,118,119,123,124,128,129,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'loop':([7,10,28,89,103,112,117,118,119,123,124,128,129,],[28,28,28,28,28,28,28,28,28,28,28,28,28,]),'forLoop':([7,10,28,89,103,112,117,118,119,123,124,128,129,],[32,32,32,32,32,32,32,32,32,32,32,32,32,]),'whileLoop':([7,10,28,89,103,112,117,118,119,123,124,128,129,],[33,33,33,33,33,33,33,33,33,33,33,33,33,]),'parameters':([56,],[80,]),'parameterList':([56,101,],[81,109,]),'parameter':([56,101,],[82,82,]),'datatype':([56,101,106,],[83,83,113,]),'function_body':([118,],[122,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> programStart','program',1,'p_program','adapscriptyacc.py',15),
  ('programStart -> FUNC INIT ( ) { statements }','programStart',7,'p_programStart','adapscriptyacc.py',19),
  ('statements -> statement','statements',1,'p_statements','adapscriptyacc.py',22),
  ('statements -> statements statement','statements',2,'p_statements','adapscriptyacc.py',23),
  ('statement -> function_calls','statement',1,'p_statement','adapscriptyacc.py',26),
  ('statement -> condition','statement',1,'p_statement','adapscriptyacc.py',27),
  ('statement -> function_declarations','statement',1,'p_statement','adapscriptyacc.py',28),
  ('statement -> expression','statement',1,'p_statement','adapscriptyacc.py',29),
  ('statement -> loops','statement',1,'p_statement','adapscriptyacc.py',30),
  ('statement -> RETURN variable','statement',2,'p_statement','adapscriptyacc.py',31),
  ('statement -> ACCEPT ( variable )','statement',4,'p_statement','adapscriptyacc.py',32),
  ('statement -> PRINT ( variable )','statement',4,'p_statement','adapscriptyacc.py',33),
  ('statement -> ACCEPT ( atoms )','statement',4,'p_statement','adapscriptyacc.py',34),
  ('statement -> PRINT ( STRING_VALUE atoms ) )','statement',6,'p_statement','adapscriptyacc.py',35),
  ('function_declarations -> function_declaration','function_declarations',1,'p_function_declarations','adapscriptyacc.py',39),
  ('function_declaration -> FUNC IDENTIFIER ( ) : datatype { function_body }','function_declaration',9,'p_function_declaration','adapscriptyacc.py',42),
  ('function_body -> statements','function_body',1,'p_function_body','adapscriptyacc.py',46),
  ('function_calls -> IDENTIFIER ( )','function_calls',3,'p_function_calls','adapscriptyacc.py',49),
  ('function_calls -> IDENTIFIER ( ) function_calls','function_calls',4,'p_function_calls','adapscriptyacc.py',50),
  ('function_calls -> IDENTIFIER ( parameters )','function_calls',4,'p_function_calls','adapscriptyacc.py',51),
  ('function_calls -> IDENTIFIER ( parameters ) function_calls','function_calls',5,'p_function_calls','adapscriptyacc.py',52),
  ('variable -> IDENTIFIER','variable',1,'p_variable','adapscriptyacc.py',55),
  ('parameters -> parameterList','parameters',1,'p_parameters','adapscriptyacc.py',58),
  ('parameterList -> parameter','parameterList',1,'p_parameterList','adapscriptyacc.py',61),
  ('parameterList -> parameter , parameterList','parameterList',3,'p_parameterList','adapscriptyacc.py',62),
  ('parameter -> datatype IDENTIFIER','parameter',2,'p_parameter','adapscriptyacc.py',65),
  ('datatype -> INT','datatype',1,'p_datatype','adapscriptyacc.py',68),
  ('datatype -> FLOAT','datatype',1,'p_datatype','adapscriptyacc.py',69),
  ('datatype -> STRING','datatype',1,'p_datatype','adapscriptyacc.py',70),
  ('datatype -> ADAPT','datatype',1,'p_datatype','adapscriptyacc.py',71),
  ('datatype -> VOID','datatype',1,'p_datatype','adapscriptyacc.py',72),
  ('atoms -> INT_VALUE','atoms',1,'p_atom','adapscriptyacc.py',75),
  ('atoms -> FLOAT_VALUE','atoms',1,'p_atom','adapscriptyacc.py',76),
  ('atoms -> STRING_VALUE','atoms',1,'p_atom','adapscriptyacc.py',77),
  ('atoms -> variable','atoms',1,'p_atom','adapscriptyacc.py',78),
  ('paren_expr -> ( expression )','paren_expr',3,'p_paren_expr','adapscriptyacc.py',81),
  ('binary_expr -> variable ADD expression','binary_expr',3,'p_binary_expr','adapscriptyacc.py',84),
  ('binary_expr -> variable SUB expression','binary_expr',3,'p_binary_expr','adapscriptyacc.py',85),
  ('binary_expr -> variable MUL expression','binary_expr',3,'p_binary_expr','adapscriptyacc.py',86),
  ('binary_expr -> variable DIV expression','binary_expr',3,'p_binary_expr','adapscriptyacc.py',87),
  ('binary_expr -> variable OR expression','binary_expr',3,'p_binary_expr','adapscriptyacc.py',88),
  ('binary_expr -> variable LE expression','binary_expr',3,'p_binary_expr','adapscriptyacc.py',89),
  ('binary_expr -> variable GE expression','binary_expr',3,'p_binary_expr','adapscriptyacc.py',90),
  ('binary_expr -> variable EQ expression','binary_expr',3,'p_binary_expr','adapscriptyacc.py',91),
  ('binary_expr -> variable NE expression','binary_expr',3,'p_binary_expr','adapscriptyacc.py',92),
  ('binary_expr -> variable GT expression','binary_expr',3,'p_binary_expr','adapscriptyacc.py',93),
  ('binary_expr -> variable LT expression','binary_expr',3,'p_binary_expr','adapscriptyacc.py',94),
  ('binary_expr -> UNARY expression','binary_expr',2,'p_binary_expr','adapscriptyacc.py',95),
  ('binary_expr -> expression UNARY','binary_expr',2,'p_binary_expr','adapscriptyacc.py',96),
  ('expression -> atoms','expression',1,'p_expression','adapscriptyacc.py',99),
  ('expression -> paren_expr','expression',1,'p_expression','adapscriptyacc.py',100),
  ('expression -> binary_expr','expression',1,'p_expression','adapscriptyacc.py',101),
  ('condition -> IF expression { statements }','condition',5,'p_condition','adapscriptyacc.py',104),
  ('condition -> IF expression { statements } ELSE { statements }','condition',9,'p_condition','adapscriptyacc.py',105),
  ('loops -> loop','loops',1,'p_loops','adapscriptyacc.py',108),
  ('loops -> loop loops','loops',2,'p_loops','adapscriptyacc.py',109),
  ('loop -> forLoop','loop',1,'p_loop','adapscriptyacc.py',113),
  ('loop -> whileLoop','loop',1,'p_loop','adapscriptyacc.py',114),
  ('forLoop -> FOR ( expression ; condition ; expression ) { statements }','forLoop',11,'p_forLoop','adapscriptyacc.py',118),
  ('whileLoop -> WHILE ( condition ) { statements }','whileLoop',7,'p_whileLoop','adapscriptyacc.py',121),
]
