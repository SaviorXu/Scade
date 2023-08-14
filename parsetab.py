
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACTIVATE AND ARROW ASSERT ASSUME AT AUTOMATON BODY BOOL CASE CHAR CLOCK COLON COMMA CONST CURRENT DEFAULT DIV DIVIDE DO ELSE ELSIF EMIT END ENUM EQU EVERY EXPONENT EXTERN FALSE FBY FINAL FLATTEN FLOAT FLOAT32 FLOAT64 FOLD FOLDI FOLDW FOLDWI FUNCTION GREATER GREATEREQU GROUP GUARANTEE HASHTAG IF IMPORTED INCLUDE INITIAL INT INT16 INT32 INT64 INT8 INTCONST INTEGER IS LAND LAST LBPARENTHESE LBRACKET LESS LESSEQU LET LNOT LOR LPARENTHESE LSHIFT LSL LSR LV6ID LV6IDREF LXOR MAKE MAP MAPFOLD MAPFOLDI MAPFOLDW MAPFOLDWI MAPI MAPW MAPWI MATCH MERGE MINUS MOD MODEL NEEDS NODE NOEQU NOR NOT NUMERIC OF OPEN OR PACKAGE PLUS POINT PRE PRIVATE PROBE PROVIDES PUBLIC RBPARENTHESE RBRACKET REAL REALCONST RESTART RESUME RETURNS REVERSE RPARENTHESE RSHIFT SEMICOLON SENSOR SHIFT SIG SIGNED SINGLEQUOTE SPECIALIZE STAR STATE STEP STRUCT SURPLUS SYNCHRO TEL THEN TIMES TPOINT TRANSPOSE TRUE TYPE UINT16 UINT32 UINT64 UINT8 UNLESS UNSAFE UNSIGNED UNTIL USES VAR VERTICALBAR WHEN WHERE WITH XOROpt_body : Simple_EquationSimple_Equation : Lhs EQU Expr SEMICOLONLhs : LV6IDExpr : Arith_expr\n          | Atom\n          | Id_exprArith_expr : Unary_arith_op Expr\n    | Expr Bin_arith_op ExprUnary_arith_op : MINUS\n    | PLUS\n    | LNOTBin_arith_op : PLUS\n    | MINUS\n    | Atom : INTCONSTId_expr : LV6ID\n    | empty empty : '
    
_lr_action_items = {'LV6ID':([0,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,],[4,12,-14,-4,-5,-6,12,-15,-16,-17,-9,-10,-11,12,-12,-13,-7,-8,]),'$end':([1,2,17,],[0,-1,-2,]),'EQU':([3,4,],[5,-3,]),'INTCONST':([5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,],[11,-14,-4,-5,-6,11,-15,-16,-17,-9,-10,-11,11,-12,-13,-7,-8,]),'MINUS':([5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,],[14,20,-4,-5,-6,14,-15,-16,-17,-9,-10,-11,14,-12,-13,20,20,]),'PLUS':([5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,],[15,19,-4,-5,-6,15,-15,-16,-17,-9,-10,-11,15,-12,-13,19,19,]),'LNOT':([5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,],[16,-14,-4,-5,-6,16,-15,-16,-17,-9,-10,-11,16,-12,-13,-7,-8,]),'SEMICOLON':([5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,],[-18,17,-4,-5,-6,-18,-15,-16,-17,-9,-10,-11,-18,-12,-13,-7,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Opt_body':([0,],[1,]),'Simple_Equation':([0,],[2,]),'Lhs':([0,],[3,]),'Expr':([5,10,18,],[6,21,22,]),'Arith_expr':([5,10,18,],[7,7,7,]),'Atom':([5,10,18,],[8,8,8,]),'Id_expr':([5,10,18,],[9,9,9,]),'Unary_arith_op':([5,10,18,],[10,10,10,]),'empty':([5,10,18,],[13,13,13,]),'Bin_arith_op':([6,21,22,],[18,18,18,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Opt_body","S'",1,None,None,None),
  ('Opt_body -> Simple_Equation','Opt_body',1,'p_opt_body','scade_compile.py',14),
  ('Simple_Equation -> Lhs EQU Expr SEMICOLON','Simple_Equation',4,'p_simple_equation','scade_compile.py',22),
  ('Lhs -> LV6ID','Lhs',1,'p_lhs','scade_compile.py',28),
  ('Expr -> Arith_expr','Expr',1,'p_expr','scade_compile.py',32),
  ('Expr -> Atom','Expr',1,'p_expr','scade_compile.py',33),
  ('Expr -> Id_expr','Expr',1,'p_expr','scade_compile.py',34),
  ('Arith_expr -> Unary_arith_op Expr','Arith_expr',2,'p_arith_expr','scade_compile.py',39),
  ('Arith_expr -> Expr Bin_arith_op Expr','Arith_expr',3,'p_arith_expr','scade_compile.py',40),
  ('Unary_arith_op -> MINUS','Unary_arith_op',1,'p_unary_arith_op','scade_compile.py',48),
  ('Unary_arith_op -> PLUS','Unary_arith_op',1,'p_unary_arith_op','scade_compile.py',49),
  ('Unary_arith_op -> LNOT','Unary_arith_op',1,'p_unary_arith_op','scade_compile.py',50),
  ('Bin_arith_op -> PLUS','Bin_arith_op',1,'p_bin_arith_op','scade_compile.py',54),
  ('Bin_arith_op -> MINUS','Bin_arith_op',1,'p_bin_arith_op','scade_compile.py',55),
  ('Bin_arith_op -> <empty>','Bin_arith_op',0,'p_bin_arith_op','scade_compile.py',56),
  ('Atom -> INTCONST','Atom',1,'p_atom','scade_compile.py',60),
  ('Id_expr -> LV6ID','Id_expr',1,'p_id_expr','scade_compile.py',65),
  ('Id_expr -> empty','Id_expr',1,'p_id_expr','scade_compile.py',66),
  ('empty -> <empty>','empty',0,'p_empty','scade_compile.py',73),
]