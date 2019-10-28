import io
import sys
sys.stdout = buffer = io.StringIO()

# from app import my_function
import pytest
import os
import app
import re
from app import start_counting
# @pytest.mark.it("1. You should change only line 3")
# def test_while_loop():
#     f = open(os.path.dirname(os.path.abspath(__file__))+ '/app.py')
#     content = f.readlines()
#     content = [x.strip() for x in content]
#     my_while = [s for s in content if "while counter > -1:" in s]
#     my_whileVar = content.index(my_while[0])
#     regex = r"while counter(\s*)>(\s*)-1:"
#     assert re.match(regex, content[my_whileVar])
@pytest.mark.it('2. Your function needs to print the correct output')
def test_for_function_output(capsys):
    start_counting()
    captured = capsys.readouterr()
    assert captured.out == "100\n99\n98\n97\n96\n95\n94\n93\n92\n91\n90\n89\n88\n87\n86\n85\n84\n83\n82\n81\n80\n79\n78\n77\n76\n75\n74\n73\n72\n71\n70\n69\n68\n67\n66\n65\n64\n63\n62\n61\n60\n59\n58\n57\n56\n55\n54\n53\n52\n51\n50\n49\n48\n47\n46\n45\n44\n43\n42\n41\n40\n39\n38\n37\n36\n35\n34\n33\n32\n31\n30\n29\n28\n27\n26\n25\n24\n23\n22\n21\n20\n19\n18\n17\n16\n15\n14\n13\n12\n11\n10\n9\n8\n7\n6\n5\n4\n3\n2\n1\n0\n"


# @pytest.mark.it('2. The console should print numbers from 100 to 1')
# def test_for_file_output(capsys):
#     def test():
#         counter = 100
#         while counter > 0:
#             print(counter)
#             counter-=1
#         return counter
#     captured = buffer.getvalue()
#     assert captured == str(test())+'\n'