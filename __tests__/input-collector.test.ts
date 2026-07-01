import { jest, test, expect } from "@jest/globals";

import * as core from "../__fixtures__/core.js";
import { ZodError } from "zod";

jest.unstable_mockModule("@actions/core", () => core)

const input_collector = await import("../src/input-collector.js");

test("test defaults", async () => {
    core.getInput.mockImplementation((inputName) => {
        if (inputName == "input_dir") return "all";
        else if (inputName == "input_file_extension") return "mmd";
        else if (inputName == "output_dir") return "same";
        else if (inputName == "output_file_extension") return "svg";
        else return "";
    })
    core.getBooleanInput.mockImplementation(() => false);
    const result = await input_collector.input_collector();

    expect(result).toStrictEqual({
        "convert_existing": false,
        "input_dir": "all",
        "input_file_extension": "mmd",
        "output_dir": "same",
        "output_file_extension": "svg"
    });
})

test("test unsupported output_file_extension", async () => {
    core.getInput.mockImplementation((inputName) => {
        if (inputName == "input_dir") return "all";
        else if (inputName == "input_file_extension") return "mmd";
        else if (inputName == "output_dir") return "same";
        else if (inputName == "output_file_extension") return "jpg";
        else return "";
    })
    core.getBooleanInput.mockImplementation(() => false);
    const result = await input_collector.input_collector();
    expect(core.setFailed).toHaveBeenCalled();
    expect(core.setFailed.mock.calls[0][0]).toMatch(/invalid option/i)
    expect(result).toStrictEqual({})
})
