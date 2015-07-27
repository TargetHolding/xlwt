class XLWTBaseException(Exception):

	pass


class XLWTWriterException(XLWTBaseException):

	pass


class XLWTCellException(XLWTBaseException):

	pass


class XLWTUnexpectedDataTypeException(XLWTCellException):

	pass


class XLWTRowOverwriteException(XLWTWriterException):

	pass


class XLWTBitmapException(XLWTBaseException):

	pass


class XLWTFormulaException(XLWTBaseException):

	pass


class XLWTStyleException(XLWTBaseException):

	pass


class XLWTFStringLengthException(XLWTBaseException):

	pass


class XLWTFColumnException(XLWTBaseException):

	pass


class XLWTColumnNotInRangeException(XLWTFColumnException):

	pass


class XLWTRowException(XLWTFColumnException):

	pass


class XLWTRowNotInRangeException(XLWTRowException):

	pass


class XLWTWorkBookException(XLWTBaseException):

	pass


class XLWTSheetException(XLWTBaseException):

	pass