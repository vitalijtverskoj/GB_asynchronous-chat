# The PEP 484 type hints stub file for the QtQuick3D module.
#
# Generated by SIP 6.7.7
#
# Copyright (c) 2023 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt5.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import typing

import PyQt5.sip

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtNetwork
from PyQt5 import QtQml

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]

# Convenient aliases for complicated OpenGL types.
PYQT_OPENGL_ARRAY = typing.Union[typing.Sequence[int], typing.Sequence[float],
        PyQt5.sip.Buffer, None]
PYQT_OPENGL_BOUND_ARRAY = typing.Union[typing.Sequence[int],
        typing.Sequence[float], PyQt5.sip.Buffer, int, None]


class QQuick3D(PyQt5.sipsimplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QQuick3D') -> None: ...

    @staticmethod
    def idealSurfaceFormat(samples: int = ...) -> QtGui.QSurfaceFormat: ...


class QQuick3DObject(QtCore.QObject, QtQml.QQmlParserStatus):

    def __init__(self, parent: typing.Optional['QQuick3DObject'] = ...) -> None: ...

    def componentComplete(self) -> None: ...
    def classBegin(self) -> None: ...
    stateChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setParentItem(self, parentItem: 'QQuick3DObject') -> None: ...
    def parentItem(self) -> 'QQuick3DObject': ...
    def setState(self, state: str) -> None: ...
    def state(self) -> str: ...


class QQuick3DGeometry(QQuick3DObject):

    class PrimitiveType(int):
        Unknown = ... # type: QQuick3DGeometry.PrimitiveType
        Points = ... # type: QQuick3DGeometry.PrimitiveType
        LineStrip = ... # type: QQuick3DGeometry.PrimitiveType
        Lines = ... # type: QQuick3DGeometry.PrimitiveType
        TriangleStrip = ... # type: QQuick3DGeometry.PrimitiveType
        TriangleFan = ... # type: QQuick3DGeometry.PrimitiveType
        Triangles = ... # type: QQuick3DGeometry.PrimitiveType

    class Attribute(PyQt5.sipsimplewrapper):

        class ComponentType(int):
            DefaultType = ... # type: QQuick3DGeometry.Attribute.ComponentType
            U16Type = ... # type: QQuick3DGeometry.Attribute.ComponentType
            U32Type = ... # type: QQuick3DGeometry.Attribute.ComponentType
            F32Type = ... # type: QQuick3DGeometry.Attribute.ComponentType

        class Semantic(int):
            UnknownSemantic = ... # type: QQuick3DGeometry.Attribute.Semantic
            IndexSemantic = ... # type: QQuick3DGeometry.Attribute.Semantic
            PositionSemantic = ... # type: QQuick3DGeometry.Attribute.Semantic
            NormalSemantic = ... # type: QQuick3DGeometry.Attribute.Semantic
            TexCoordSemantic = ... # type: QQuick3DGeometry.Attribute.Semantic
            TangentSemantic = ... # type: QQuick3DGeometry.Attribute.Semantic
            BinormalSemantic = ... # type: QQuick3DGeometry.Attribute.Semantic

        componentType = ... # type: 'QQuick3DGeometry.Attribute.ComponentType'
        offset = ... # type: int
        semantic = ... # type: 'QQuick3DGeometry.Attribute.Semantic'

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QQuick3DGeometry.Attribute') -> None: ...

    def __init__(self, parent: typing.Optional[QQuick3DObject] = ...) -> None: ...

    nameChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setName(self, name: str) -> None: ...
    def clear(self) -> None: ...
    @typing.overload
    def addAttribute(self, semantic: 'QQuick3DGeometry.Attribute.Semantic', offset: int, componentType: 'QQuick3DGeometry.Attribute.ComponentType') -> None: ...
    @typing.overload
    def addAttribute(self, att: 'QQuick3DGeometry.Attribute') -> None: ...
    def setPrimitiveType(self, type: 'QQuick3DGeometry.PrimitiveType') -> None: ...
    def setBounds(self, min: QtGui.QVector3D, max: QtGui.QVector3D) -> None: ...
    def setStride(self, stride: int) -> None: ...
    def setIndexData(self, data: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> None: ...
    def setVertexData(self, data: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> None: ...
    def stride(self) -> int: ...
    def boundsMax(self) -> QtGui.QVector3D: ...
    def boundsMin(self) -> QtGui.QVector3D: ...
    def primitiveType(self) -> 'QQuick3DGeometry.PrimitiveType': ...
    def attribute(self, index: int) -> 'QQuick3DGeometry.Attribute': ...
    def attributeCount(self) -> int: ...
    def indexBuffer(self) -> QtCore.QByteArray: ...
    def vertexBuffer(self) -> QtCore.QByteArray: ...
    def name(self) -> str: ...
