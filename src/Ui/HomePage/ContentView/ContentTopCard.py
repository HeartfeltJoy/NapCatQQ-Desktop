# -*- coding: utf-8 -*-
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget
from qfluentwidgets import CaptionLabel, TitleLabel


class ContentTopCard(QWidget):
    """
    ## ContentViewWidget 顶部展示的 InputCard
    """

    def __init__(self, parent) -> None:
        super().__init__(parent=parent)

        # 创建所需控件
        self.titleLabel = TitleLabel(self.tr("NapCat Dashboard"), self)
        self.subtitleLabel = CaptionLabel(self.tr("Here you may have the data you're interested in"), self)

        self.hBoxLayout = QHBoxLayout()
        self.labelLayout = QVBoxLayout()
        self.buttonLayout = QHBoxLayout()

        # 调用方法
        self._setLayout()

    def _setLayout(self) -> None:
        """
        ## 对内部进行布局
        """
        self.labelLayout.setSpacing(0)
        self.labelLayout.setContentsMargins(0, 0, 0, 0)
        self.labelLayout.addWidget(self.titleLabel)
        self.labelLayout.addSpacing(5)
        self.labelLayout.addWidget(self.subtitleLabel)

        self.buttonLayout.setSpacing(0)
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonLayout.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)

        self.hBoxLayout.addLayout(self.labelLayout)
        self.hBoxLayout.addLayout(self.buttonLayout)
        self.hBoxLayout.setContentsMargins(0, 0, 20, 0)

        self.setLayout(self.hBoxLayout)
