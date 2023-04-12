<<<<<<< HEAD
from controlo_react.reaccoes.recolher import Recolher
from ecr.comport_comp import ComportComp
from ecr.hierarquia import Hierarquia
from sae import Simulador

from controlo_react.controlo_react import ControloReact
from controlo_react.reaccoes.explorar.explorar import Explorar


comportamento = Recolher()

controlo = ControloReact(comportamento)
=======
from controlo_react.reaccoes.recolher import Recolher
from ecr.comport_comp import ComportComp
from ecr.hierarquia import Hierarquia
from sae import Simulador

from controlo_react.controlo_react import ControloReact
from controlo_react.reaccoes.explorar.explorar import Explorar


comportamento = Recolher()

controlo = ControloReact(comportamento)
>>>>>>> 3976a3f6da1b734f3b7d4dc5030b32391c3adfcb
Simulador(1, controlo).executar()