import unittest
import os

from AlphaTwirl.Configure import TableConfigCompleter

##__________________________________________________________________||
class MockDefaultSummary: pass

##__________________________________________________________________||
class MockSummary2: pass

##__________________________________________________________________||
class MockWeight: pass

##__________________________________________________________________||
class MockBinning: pass

##__________________________________________________________________||
class TestTableConfigCompleter(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_copy_not_the_same_object(self):
        obj = TableConfigCompleter(
            defaultSummaryClass = MockDefaultSummary,
            defaultWeight = MockWeight(),
            defaultOutDir = 'tmp'
        )
        tblcfg_in = dict(keyAttrNames = ('met_pt', ), binnings = (MockBinning(), ))
        tblcfg_out = obj.complete(tblcfg_in)
        self.assertIsNot(tblcfg_in, tblcfg_out)

    def test_empty_input(self):
        defaultWeight = MockWeight()
        obj = TableConfigCompleter(
            defaultSummaryClass = MockDefaultSummary,
            defaultWeight = defaultWeight,
            defaultOutDir = 'tmp'
        )

        expected = dict(
            keyAttrNames = (),
            keyIndices = None,
            binnings = None,
            keyOutColumnNames = (),
            valAttrNames = None,
            valIndices = None,
            summaryClass = MockDefaultSummary,
            valOutColumnNames = ('n', 'nvar'),
            weight = defaultWeight,
            sort = True,
            nevents = None,
            outFile = True,
            outFileName = 'tbl_n_component.txt',
            outFilePath = 'tmp/tbl_n_component.txt',
        )

        tblcfg = dict()
        actual = obj.complete(tblcfg)

        self.assertEqual(actual, expected)

    def test_simple_input(self):

        defaultWeight = MockWeight()
        obj = TableConfigCompleter(
            defaultSummaryClass = MockDefaultSummary,
            defaultWeight = defaultWeight,
            defaultOutDir = 'tmp'
        )

        binning1 = MockBinning()

        expected = dict(
            keyAttrNames = ('met_pt',),
            keyIndices = None,
            binnings = (binning1, ),
            keyOutColumnNames = ('met_pt',),
            valAttrNames = None,
            valIndices = None,
            summaryClass = MockDefaultSummary,
            valOutColumnNames = ('n', 'nvar'),
            weight = defaultWeight,
            sort = True,
            nevents = None,
            outFile = True,
            outFileName = 'tbl_n_component_met_pt.txt',
            outFilePath = 'tmp/tbl_n_component_met_pt.txt',
        )

        tblcfg = dict(
            keyAttrNames = ('met_pt', ),
            binnings = (binning1, )
        )

        actual = obj.complete(tblcfg)

        self.assertEqual(actual, expected)


    def test_default_summary_class_empty_key(self):

        defaultWeight = MockWeight()
        obj = TableConfigCompleter(
            defaultSummaryClass = MockDefaultSummary,
            defaultWeight = defaultWeight,
            defaultOutDir = 'tmp'
        )

        expected = dict(
            keyAttrNames = (),
            keyIndices = None,
            binnings = (),
            keyOutColumnNames = (),
            valAttrNames = None,
            valIndices = None,
            summaryClass = MockDefaultSummary,
            valOutColumnNames = ('n', 'nvar'),
            weight = defaultWeight,
            sort = True,
            nevents = None,
            outFile = True,
            outFileName = 'tbl_n_component.txt',
            outFilePath = 'tmp/tbl_n_component.txt',
        )

        tblcfg = dict(
            keyAttrNames = ( ),
            binnings = ( )
        )

        actual = obj.complete(tblcfg)

        self.assertEqual(actual, expected)


    def test_specify_summary_class_empty_key_empty_val(self):

        defaultWeight = MockWeight()
        obj = TableConfigCompleter(
            defaultSummaryClass = MockDefaultSummary,
            defaultWeight = defaultWeight,
            defaultOutDir = 'tmp'
        )

        expected = dict(
            keyAttrNames = (),
            keyIndices = None,
            binnings = (),
            keyOutColumnNames = (),
            valAttrNames = None,
            valIndices = None,
            summaryClass = MockSummary2,
            valOutColumnNames = (),
            weight = defaultWeight,
            sort = True,
            nevents = None,
            outFile = True,
            outFileName = 'tbl_MockSummary2.txt',
            outFilePath = 'tmp/tbl_MockSummary2.txt',
        )

        tblcfg = dict(
            keyAttrNames = ( ),
            binnings = ( ),
            summaryClass = MockSummary2,
        )

        actual = obj.complete(tblcfg)

        self.assertEqual(actual, expected)


    def test_specify_summary_class_2_keys_empty_vals(self):

        defaultWeight = MockWeight()
        obj = TableConfigCompleter(
            defaultSummaryClass = MockDefaultSummary,
            defaultWeight = defaultWeight,
            defaultOutDir = 'tmp'
        )

        binning1 = MockBinning()
        binning2 = MockBinning()

        expected = dict(
            keyAttrNames = ('key1', 'key2'),
            keyIndices = None,
            binnings = (binning1, binning2),
            keyOutColumnNames = ('key1', 'key2'),
            valAttrNames = None,
            valIndices = None,
            summaryClass = MockSummary2,
            valOutColumnNames = (),
            weight = defaultWeight,
            sort = True,
            nevents = None,
            outFile = True,
            outFileName = 'tbl_MockSummary2_key1_key2.txt',
            outFilePath = 'tmp/tbl_MockSummary2_key1_key2.txt',
        )

        tblcfg = dict(
            keyAttrNames = ('key1', 'key2'),
            binnings = (binning1, binning2),
            summaryClass = MockSummary2,
        )

        actual = obj.complete(tblcfg)

        self.assertEqual(actual, expected)


    def test_specify_summary_class_2_keys_2_vals(self):

        defaultWeight = MockWeight()
        obj = TableConfigCompleter(
            defaultSummaryClass = MockDefaultSummary,
            defaultWeight = defaultWeight,
            defaultOutDir = 'tmp'
        )

        binning1 = MockBinning()
        binning2 = MockBinning()

        expected = dict(
            keyAttrNames = ('key1', 'key2'),
            keyIndices = None,
            binnings = (binning1, binning2),
            keyOutColumnNames = ('key1', 'key2'),
            valAttrNames = ('val1', 'val2'),
            valIndices = None,
            summaryClass = MockSummary2,
            valOutColumnNames = ('val1', 'val2'),
            weight = defaultWeight,
            sort = True,
            nevents = None,
            outFile = True,
            outFileName = 'tbl_MockSummary2_key1_key2_val1_val2.txt',
            outFilePath = 'tmp/tbl_MockSummary2_key1_key2_val1_val2.txt',
        )

        tblcfg = dict(
            keyAttrNames = ('key1', 'key2'),
            binnings = (binning1, binning2),
            valAttrNames = ('val1', 'val2'),
            summaryClass = MockSummary2,
        )

        actual = obj.complete(tblcfg)

        self.assertEqual(actual, expected)


    def test_specify_summary_class_2_keys_2_vals_key_indices(self):

        defaultWeight = MockWeight()
        obj = TableConfigCompleter(
            defaultSummaryClass = MockDefaultSummary,
            defaultWeight = defaultWeight,
            defaultOutDir = 'tmp'
        )

        binning1 = MockBinning()
        binning2 = MockBinning()

        expected = dict(
            keyAttrNames = ('key1', 'key2'),
            keyIndices = (None, 1),
            binnings = (binning1, binning2),
            keyOutColumnNames = ('key1', 'key2'),
            valAttrNames = ('val1', 'val2'),
            valIndices = None,
            summaryClass = MockSummary2,
            valOutColumnNames = ('val1', 'val2'),
            weight = defaultWeight,
            sort = True,
            nevents = None,
            outFile = True,
            outFileName = 'tbl_MockSummary2_key1_key2_1_val1_val2.txt',
            outFilePath = 'tmp/tbl_MockSummary2_key1_key2_1_val1_val2.txt',
        )

        tblcfg = dict(
            keyAttrNames = ('key1', 'key2'),
            binnings = (binning1, binning2),
            keyIndices = (None, 1),
            valAttrNames = ('val1', 'val2'),
            summaryClass = MockSummary2,
        )

        actual = obj.complete(tblcfg)

        self.assertEqual(actual, expected)


    def test_specify_summary_class_2_keys_2_vals_val_indices(self):

        defaultWeight = MockWeight()
        obj = TableConfigCompleter(
            defaultSummaryClass = MockDefaultSummary,
            defaultWeight = defaultWeight,
            defaultOutDir = 'tmp'
        )

        binning1 = MockBinning()
        binning2 = MockBinning()

        expected = dict(
            keyAttrNames = ('key1', 'key2'),
            keyIndices = None,
            binnings = (binning1, binning2),
            keyOutColumnNames = ('key1', 'key2'),
            valAttrNames = ('val1', 'val2'),
            valIndices = (2, None),
            summaryClass = MockSummary2,
            valOutColumnNames = ('val1', 'val2'),
            weight = defaultWeight,
            sort = True,
            nevents = None,
            outFile = True,
            outFileName = 'tbl_MockSummary2_key1_key2_val1_2_val2.txt',
            outFilePath = 'tmp/tbl_MockSummary2_key1_key2_val1_2_val2.txt',
        )

        tblcfg = dict(
            keyAttrNames = ('key1', 'key2'),
            binnings = (binning1, binning2),
            valAttrNames = ('val1', 'val2'),
            summaryClass = MockSummary2,
            valIndices = (2, None),
        )

        actual = obj.complete(tblcfg)

        self.assertEqual(actual, expected)


    def test_specify_summary_class_2_keys_2_vals_key_indices_val_indices(self):

        defaultWeight = MockWeight()
        obj = TableConfigCompleter(
            defaultSummaryClass = MockDefaultSummary,
            defaultWeight = defaultWeight,
            defaultOutDir = 'tmp'
        )

        binning1 = MockBinning()
        binning2 = MockBinning()

        expected = dict(
            keyAttrNames = ('key1', 'key2'),
            keyIndices = (None, 1),
            binnings = (binning1, binning2),
            keyOutColumnNames = ('key1', 'key2'),
            valAttrNames = ('val1', 'val2'),
            valIndices = (2, 3),
            summaryClass = MockSummary2,
            valOutColumnNames = ('val1', 'val2'),
            weight = defaultWeight,
            sort = True,
            nevents = None,
            outFile = True,
            outFileName = 'tbl_MockSummary2_key1_key2_1_val1_2_val2_3.txt',
            outFilePath = 'tmp/tbl_MockSummary2_key1_key2_1_val1_2_val2_3.txt',
        )

        tblcfg = dict(
            keyAttrNames = ('key1', 'key2'),
            binnings = (binning1, binning2),
            keyIndices = (None, 1),
            valAttrNames = ('val1', 'val2'),
            summaryClass = MockSummary2,
            valIndices = (2, 3),
        )

        actual = obj.complete(tblcfg)

        self.assertEqual(actual, expected)

##__________________________________________________________________||
